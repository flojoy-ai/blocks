import ast
import json
import os
from typing import Optional, cast

from docstring_parser import parse
from rich import print

from cli.constants import BLOCKS_FOLDER, ERR_STRING


def generate_docstring_json() -> bool:
    """
    Will return True if all the docstrings are formatted correctly
    False if there is any docstring format error
    """

    errors = 0

    # Walk through all the folders and files in the current directory
    for root, _, files in os.walk(BLOCKS_FOLDER):
        # Iterate through the files
        for file in files:
            # Check if the file is a Python file and has the same name as the folder
            is_block_file = file.endswith(
                ".py") and file[:-3] == os.path.basename(root)
            if not is_block_file:
                continue

            # Construct the file path
            file_path = os.path.join(root, file)

            # Read the contents of the Python file
            with open(file_path, "r") as f:
                code = f.read()

                block_name = os.path.basename(root)
                docstring = _get_docstring(code, block_name)
                if docstring is None:
                    print(f"{ERR_STRING} Docstring not found for {block_name}")
                    errors += 1
                    continue

                # Process the docstring using docstring_parser
                parsed_docstring = parse(docstring)

                if not parsed_docstring.short_description:
                    print(
                        f"{ERR_STRING} short_description not found for {block_name}"
                    )
                    errors += 1

                # it is okay to not have a long description
                if not parsed_docstring.long_description:
                    parsed_docstring.long_description = ""

                if not parsed_docstring.params:
                    print(
                        f"{ERR_STRING} 'Parameters' not found for {block_name}"
                    )
                    errors += 1

                if not parsed_docstring.many_returns:
                    print(f"{ERR_STRING} 'Returns' not found for {block_name}")
                    errors += 1

                # Build the JSON data
                json_data = {
                    "long_description":
                    parsed_docstring.long_description,
                    "short_description":
                    parsed_docstring.short_description,
                    "parameters": [{
                        "name": param.arg_name,
                        "type": param.type_name,
                        "description": param.description,
                    } for param in parsed_docstring.params],
                    "returns": [{
                        "name": rtn.return_name,
                        "type": rtn.type_name,
                        "description": rtn.description,
                    } for rtn in parsed_docstring.many_returns],
                }

                # Write the data to a JSON file in the same directory
                output_file_path = os.path.join(root, "docstring.json")
                with open(output_file_path, "w") as output_file:
                    json.dump(json_data, output_file, indent=2)

    if errors > 0:
        print(
            f"Found {errors} [bold red]ERRORS[/bold red] with docstring formatting!"
        )
        return False

    print("[bold green] All docstring are formatted correctly!")
    return True


def _get_docstring(code: str, block_name: str) -> Optional[str]:
    # Parse the code
    tree = ast.parse(code)

    # Find functions in the code
    for node in ast.walk(tree):
        if not isinstance(node, ast.FunctionDef):
            continue

        # don't parse for any function that has a different
        # name than the node file name
        function_name = node.name
        if function_name != block_name:
            continue

        # Extract docstring if available
        has_docstring = (node.body and isinstance(node.body[0], ast.Expr)
                         and isinstance(node.body[0].value, ast.Str))
        if not has_docstring:
            return None

        docstring_node = cast(ast.Str, cast(ast.Expr, node.body[0]).value)
        return docstring_node.s
