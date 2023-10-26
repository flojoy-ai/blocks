import json
import os
import sys

from rich import print

from cli.constants import BLOCKS_FOLDER, DOCS_FOLDER, ERR_STRING
from cli.state import state
from cli.utils.block_docs_builder import BlockDocsBuilder
from cli.utils.generate_docstring_json import generate_docstring_json

REQUIRED_SKIP_IF_AUTOGEN = ["example.md", "app.json"]
REQUIRED_EXAMPLE_FILES = ["docstring.json"]
AUTOGEN_CATEGORIES = ["NUMPY", "SCIPY"]
KEEP_FILES = ["overview.mdx"]


def sync():
    """
    This sync command will only operate on the blocks folder as well as the
    blocks folder in the docs folder.
    """
    total_synced_pages = 0

    # We would like to NOT modify the following files

    print("Generating docstring.json for all the blocks...")
    success = generate_docstring_json()
    if not success:
        print(
            f"{ERR_STRING} Please fix all the docstring errors before syncing."
        )
        sys.exit(1)

    print(f"Cleaning the blocks section except all the {KEEP_FILES} files.")
    for root, _, files in os.walk(DOCS_FOLDER, topdown=False):
        for file in files:
            if file in KEEP_FILES:
                continue
            file_path = os.path.join(root, file)
            os.remove(file_path)

    print("Populating the blocks section...")
    for root, _, files in os.walk(BLOCKS_FOLDER):
        folder_name = os.path.basename(root)

        for file in files:
            file_name = os.path.splitext(file)[0]

            if file_name != folder_name:
                continue
            # In this case we found the Python file that matches the folder

            if state["verbose"]:
                print(f"Processing {file_name}")

            # example: VISUALIZERS/DATA_STRUCTURE/ARRAY_VIEW
            block_folder_path = root.split("blocks", 1)[1].strip("/")
            block_category = block_folder_path.split("/")[0]
            autogen = block_category in AUTOGEN_CATEGORIES
            required_files = (REQUIRED_EXAMPLE_FILES
                              if autogen else REQUIRED_EXAMPLE_FILES +
                              REQUIRED_SKIP_IF_AUTOGEN)

            for required_file in required_files:
                if not os.path.exists(os.path.join(root, required_file)):
                    print(
                        f"{ERR_STRING} No {required_file} found for {file_name}"
                    )
                    sys.exit(1)

            with open(os.path.join(root, "docstring.json"), "r") as f:
                description = json.load(f)["short_description"]

            target_md_file = DOCS_FOLDER + block_folder_path + ".mdx"
            os.makedirs(os.path.dirname(target_md_file), exist_ok=True)

            with open(target_md_file, "w") as f:
                # Write the content of the markdown file
                result = (BlockDocsBuilder(
                    block_name=file_name,
                    block_folder_path=block_folder_path,
                    description=description,
                ).add_python_docs_display().add_python_code())

                if not autogen:
                    result = result.add_example_app()

                f.write(result.build())

            total_synced_pages += 1

    print("Almost done! Doing some housekeeping...")
    for root, _, files in os.walk("."):
        for file in files:
            if file == ".DS_Store":
                file_path = os.path.join(root, file)
                os.remove(file_path)

    for dirpath, dirnames, filenames in os.walk(DOCS_FOLDER):
        if not filenames and not dirnames:
            os.rmdir(dirpath)

    for dirpath, dirnames, filenames in os.walk(BLOCKS_FOLDER):
        if not filenames and not dirnames:
            os.rmdir(dirpath)

    print(
        f"[bold green] Successfully synced {total_synced_pages} block pages!")
