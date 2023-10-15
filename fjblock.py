import os
import re
import sys

import typer
from rich import print
from rich.console import Console

err_console = Console(stderr=True)
app = typer.Typer()

err_string = "[bold red]Error![/bold red]"


docs_folder_prefix = "docs/src/content/docs/blocks"
blocks_folder_prefix = "blocks"


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
title: {block_name}
---

Here you can write the docs for your {block_name} block.

"""


@app.command()
def sync():
    pass


@app.command()
def add(block: str):
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
