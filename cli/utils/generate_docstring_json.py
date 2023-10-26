import ast
import json
import os
from typing import cast

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

            # Parse the code
            tree = ast.parse(code)

            # Find functions in the code
            for node in ast.walk(tree):
                if not isinstance(node, ast.FunctionDef):
                    continue

                # don't parse for any function that has a different
                # name than the node file name
                function_name = node.name
                if function_name != os.path.basename(root):
                    continue

                # Extract docstring if available
                has_docstring = (node.body
                                 and isinstance(node.body[0], ast.Expr)
                                 and isinstance(node.body[0].value, ast.Str))
                if not has_docstring:
                    print(
                        f"{ERR_STRING} Docstring not found for {function_name}"
                    )
                    errors += 1
                    continue

                docstring_node = cast(ast.Str,
                                      cast(ast.Expr, node.body[0]).value)
                docstring = docstring_node.s

                try:
                    _write_docstring(docstring, root)
                except ValueError as e:
                    print(f"{ERR_STRING} {str(e)} for {function_name}")
                    errors += 1

    if errors > 0:
        print(
            f"Found {errors} [bold red]ERRORS[/bold red] with docstring formatting!"
        )
        return False

    print("[bold green] All docstring are formatted correctly!")
    return True


def _write_docstring(docstring: str, path: str):
    """Process the docstring using docstring_parser and write it to a file.
    Raises an error if short_description, parameters, or returns are missing.
    """
    # Process the docstring using docstring_parser
    parsed_docstring = parse(docstring)

    if not parsed_docstring.short_description:
        raise ValueError("short_description not found")

    # it is okay to not have a long description
    if not parsed_docstring.long_description:
        parsed_docstring.long_description = ""

    if not parsed_docstring.params:
        raise ValueError("'Parameters' not found")

    if not parsed_docstring.many_returns:
        raise ValueError("'Returns' not found")

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
    output_file_path = os.path.join(path, "docstring.json")
    with open(output_file_path, "w") as output_file:
        json.dump(json_data, output_file, indent=2)
