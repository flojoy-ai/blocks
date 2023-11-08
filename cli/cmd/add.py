import os
import re
import sys

from rich import print

from cli.constants import BLOCK_TEMPLATE, BLOCKS_SOURCE_FOLDER, ERR_STRING
from cli.logging import err_console


def add(block: str):
    # TODO: Update the add command once everything else is done

    # first we verify if the block name is valid
    parts = block.split(".")
    block_name = parts[-1]
    pattern = r"^(?!^\d)[A-Z0-9_]+$"
    for part in parts:
        if part == "":
            err_console.print(
                f"{ERR_STRING} you cannot have empty part in your block name!"
            )
            sys.exit(1)

        match = re.match(pattern, part)
        if not match:
            err_console.print(
                f"{ERR_STRING} {part} is not a valid block name. It can only include uppercase alphanumeric characters and underscores. It also cannot start with a number."
            )
            sys.exit(1)

    # if it is valid, we can start scaffolding the boilerplate

    # lastly we finish with the python block code
    blocks_target_path = os.path.join(BLOCKS_SOURCE_FOLDER, block.replace(".", "/"))
    os.makedirs(blocks_target_path, exist_ok=True)

    with open(os.path.join(blocks_target_path, f"{block_name}.py"), "w+") as f:
        f.write(BLOCK_TEMPLATE.format(block_name=block_name))

    with open(os.path.join(blocks_target_path, "example.md"), "w+") as f:
        f.write("Placeholder for the example app's description")

    print(f"Done! Your Flojoy Block is ready at '{blocks_target_path}'")
