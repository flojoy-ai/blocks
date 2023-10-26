import json
import os
import sys

from rich import print

from cli.constants import BLOCKS_DOCS_FOLDER, BLOCKS_SOURCE_FOLDER, ERR_STRING
from cli.state import state
from cli.utils.block_docs_builder import BlockDocsBuilder
from cli.utils.generate_docstring_json import generate_docstring_json


def sync():
    """
    This sync command will only operate on the blocks folder as well as the
    blocks folder in the docs folder.
    """
    total_synced_pages = 0

    # We would like to NOT modify the following files
    keep_files = ["overview.mdx"]
    auto_gen_categories = ["NUMPY", "SCIPY"]

    print("Generating docstring.json for all the blocks...")
    success = generate_docstring_json()
    if not success:
        print(f"{ERR_STRING} Please fix all the docstring errors before syncing.")
        sys.exit(1)

    print(f"Cleaning the blocks section except all the {keep_files} files.")
    for root, _, files in os.walk(BLOCKS_DOCS_FOLDER, topdown=False):
        for file in files:
            if file in keep_files:
                continue
            file_path = os.path.join(root, file)
            os.remove(file_path)

    print("Populating the blocks section...")
    for root, _, files in os.walk(BLOCKS_SOURCE_FOLDER):
        folder_name = os.path.basename(root)

        for file in files:
            file_name = os.path.splitext(file)[0]

            if file_name != folder_name:
                continue

            # In this case we found the Python file that matches the folder

            if state["verbose"]:
                print(f"Processing {file_name}")

            # example: VISUALIZERS/DATA_STRUCTURE/ARRAY_VIEW
            current_block_folder_path = root.split("blocks", 1)[1].strip("/")

            current_block_category = current_block_folder_path.split("/")[0]

            if not os.path.exists(os.path.join(root, "example.md")):
                if current_block_category not in auto_gen_categories:
                    print(f"{ERR_STRING} No example.md found for {file_name}")
                    sys.exit(1)

            if not os.path.exists(os.path.join(root, "app.json")):
                if current_block_category not in auto_gen_categories:
                    print(f"{ERR_STRING} No app.json found for {file_name}")
                    sys.exit(1)

            if not os.path.exists(os.path.join(root, "docstring.json")):
                print(f"{ERR_STRING} No docstring.json found for {file_name}")
                sys.exit(1)

            with open(os.path.join(root, "docstring.json"), "r") as f:
                description = json.load(f)["short_description"]

            # Create the markdown template file in docs
            target_md_file = BLOCKS_DOCS_FOLDER + os.path.join(
                current_block_folder_path + ".mdx"
            )

            os.makedirs(os.path.dirname(target_md_file), exist_ok=True)

            with open(target_md_file, "w") as f:
                # Write the content of the markdown file
                result = (
                    BlockDocsBuilder(
                        block_name=file_name,
                        block_folder_path=current_block_folder_path,
                        description=description,
                    )
                    .add_python_docs_display()
                    .add_python_code()
                )

                if current_block_category not in auto_gen_categories:
                    result = result.add_example_app()

                f.write(result.build())

            total_synced_pages += 1

    # Remove all empty folders
    print("Almost done! Doing some housekeeping...")

    for root, _, files in os.walk("."):
        for file in files:
            if file == ".DS_Store":
                file_path = os.path.join(root, file)
                os.remove(file_path)

    for dirpath, dirnames, filenames in os.walk(BLOCKS_DOCS_FOLDER):
        if (
            not filenames and not dirnames
        ):  # Check if the directory has no files or subdirectories
            os.rmdir(dirpath)  # Remove the directory

    for dirpath, dirnames, filenames in os.walk(BLOCKS_SOURCE_FOLDER):
        if (
            not filenames and not dirnames
        ):  # Check if the directory has no files or subdirectories
            os.rmdir(dirpath)  # Remove the directory

    print(f"Successfully synced {total_synced_pages} block pages!")
