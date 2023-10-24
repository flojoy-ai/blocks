import os
import sys

from rich import print

from cli.constants import blocks_folder_prefix, docs_folder_prefix, err_string
from cli.state import state
from cli.utils.block_docs_builder import BlockDocsBuilder


def sync():
    """
    This sync command will only operate on the blocks folder as well as the
    blocks folder in the docs folder.
    """
    total_synced_pages = 0

    # We would like to NOT modify the following files
    keep_files = ["overview.md"]
    auto_gen_categories = ["NUMPY", "SCIPY"]

    print(f"Cleaning the blocks section except all the {keep_files} files.")
    for root, _, files in os.walk(docs_folder_prefix, topdown=False):
        for file in files:
            if file in keep_files:
                continue
            file_path = os.path.join(root, file)
            os.remove(file_path)

    print("Populating the blocks section...")
    for root, _, files in os.walk(blocks_folder_prefix):
        folder_name = os.path.basename(root)

        for file in files:
            file_name = os.path.splitext(file)[0]

            if file_name == folder_name:
                # In this case we found the Python file that matches the folder

                if state["verbose"]:
                    print(f"Processing {file_name}")

                # example: VISUALIZERS/DATA_STRUCTURE/ARRAY_VIEW
                block_folder_path = root.split("blocks", 1)[1].strip("/")

                block_category = block_folder_path.split("/")[0]

                if not os.path.exists(os.path.join(root, "example.md")):
                    if block_category in auto_gen_categories:
                        pass
                    else:
                        print(f"{err_string} No example.md found for {file_name}")
                        sys.exit(1)

                if not os.path.exists(os.path.join(root, "app.json")):
                    if block_category in auto_gen_categories:
                        pass
                    else:
                        print(f"{err_string} No app.json found for {file_name}")
                        sys.exit(1)

                # Create the markdown template file in docs

                target_md_file = docs_folder_prefix + os.path.join(
                    block_folder_path + ".mdx"
                )

                os.makedirs(os.path.dirname(target_md_file), exist_ok=True)

                with open(target_md_file, "w") as f:
                    # Write the content of the markdown file
                    if block_category in auto_gen_categories:
                        result = (
                            BlockDocsBuilder(
                                block_name=file_name,
                                block_folder_path=block_folder_path,
                            )
                            .add_python_docs_display()
                            .add_python_code()
                            .build()
                        )
                    else:
                        result = (
                            BlockDocsBuilder(
                                block_name=file_name,
                                block_folder_path=block_folder_path,
                            )
                            .add_python_docs_display()
                            .add_python_code()
                            .add_example_app()
                            .build()
                        )
                    f.write(result)

                total_synced_pages += 1

    # Remove all empty folders
    print("Almost done! Doing some housekeeping...")
    for dirpath, dirnames, filenames in os.walk(docs_folder_prefix):
        if (
            not filenames and not dirnames
        ):  # Check if the directory has no files or subdirectories
            os.rmdir(dirpath)  # Remove the directory

    print(f"Successfully synced {total_synced_pages} pages!")
