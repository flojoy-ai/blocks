import os
import re
import sys

import typer
from rich import print
from rich.console import Console

err_console = Console(stderr=True)
app = typer.Typer()

err_string = "[bold red]Error![/bold red]"

github_base = "https://github.com/flojoy-ai/blocks/blob/main/blocks/{block_folder_path}/{block_name}.py"

docs_folder_prefix = "docs/src/content/docs/blocks/"
blocks_folder_prefix = "blocks/"

block_template = """\
from flojoy import flojoy, DataContainer


@flojoy
def {block_name}(
    default: DataContainer,
) -> DataContainer:
    pass
"""

docs_template = """\
---
layout: "@/layouts/block-docs-layout.astro"
title: {block_name}
---

import docstring from "@blocks/{block_folder_path}/docstring.json";
import app from "@blocks/{block_folder_path}/app.json";
import PythonDocsDisplay from "@/components/python-docs-display.astro";
import AppDisplay from "@/components/app-display.tsx";

<PythonDocsDisplay docstring={{docstring}} />
<AppDisplay app={{app}} client:visible />

<details>
<summary>Python Code</summary>
```python
{python_code}
```
[Find this Flojoy Block on GitHub]({github_link})
</details>


## Example
"""


@app.command()
def sync():
    keep_files = ["overview.md"]

    print(f"Cleaning the blocks section except all the {keep_files} files.")
    for root, _, files in os.walk(docs_folder_prefix, topdown=False):
        # Remove files except for "intro.md"
        for file in files:
            if file in keep_files:
                continue
            file_path = os.path.join(root, file)
            os.remove(file_path)

    print("Populating the blocks section...")
    for root, _, files in os.walk(blocks_folder_prefix):
        for file in files:
            folder_name = os.path.basename(root)
            file_name = os.path.splitext(file)[0]

            if file_name == folder_name:
                with open(os.path.join(root, file), "r") as f:
                    python_code = f.read()

                # Create the markdown file in another directory
                block_folder_path = root.split("blocks", 1)[1].strip("/")
                target_md_file = docs_folder_prefix + os.path.join(
                    block_folder_path + ".mdx"
                )

                os.makedirs(os.path.dirname(target_md_file), exist_ok=True)

                with open(target_md_file, "w") as f:
                    # Write the content of the markdown file
                    f.write(
                        docs_template.format(
                            block_name=file_name,
                            block_folder_path=block_folder_path,
                            python_code=python_code,
                            github_link=github_base.format(
                                block_name=file_name,
                                block_folder_path=block_folder_path,
                            ),
                        )
                    )

    # Remove all empty folders
    print("Almost done! Doing some housekeeping...")
    for dirpath, dirnames, filenames in os.walk(docs_folder_prefix):
        if (
            not filenames and not dirnames
        ):  # Check if the directory has no files or subdirectories
            os.rmdir(dirpath)  # Remove the directory


@app.command()
def add(block: str):
    # TODO: Update the add command once everything else is done

    # first we verify if the block name is valid
    parts = block.split(".")
    block_name = parts[-1]
    pattern = r"^(?!^\d)\w+$"
    for part in parts:
        if part == "":
            err_console.print(
                f"{err_string} you cannot have empty part in your block name!"
            )
            sys.exit(1)

        match = re.match(pattern, part)
        if not match:
            err_console.print(
                f"{err_string} {part} is not a valid block name. It can only include alphanumeric characters and underscores. It also cannot start with a number."
            )
            sys.exit(1)

    # if it is valid, we can start scaffolding the boilerplate

    # let's first start with the docs

    docs_target_path = os.path.dirname(
        os.path.join(docs_folder_prefix, block.replace(".", "/"))
    )
    os.makedirs(docs_target_path, exist_ok=True)
    with open(os.path.join(docs_target_path, f"{block_name}.md"), "w+") as f:
        f.write(docs_template.format(block_name=block_name))

    # lastly we finish with the python block code
    blocks_target_path = os.path.join(blocks_folder_prefix, block.replace(".", "/"))
    os.makedirs(blocks_target_path, exist_ok=True)
    with open(os.path.join(blocks_target_path, f"{block_name}.py"), "w+") as f:
        f.write(block_template.format(block_name=block_name))

    print(
        f"Done! Checkout your '{docs_target_path}' and '{blocks_target_path}' folders for the boiletplates."
    )


if __name__ == "__main__":
    # this is to make sure we are running the cli in the right directory
    required_folders = [docs_folder_prefix, blocks_folder_prefix]
    if not all([os.path.isdir(folder) for folder in required_folders]):
        err_console.print(
            f"{err_string} fjblock.py must be run at a directory where the following folders are present: {required_folders}"
        )
        sys.exit(1)

    app()
