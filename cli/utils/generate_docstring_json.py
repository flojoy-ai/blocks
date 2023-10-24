import ast
import json
import os

from docstring_parser import parse
from rich import print

from cli.constants import blocks_folder_prefix, err_string, warn_string


def generate_docstring_json() -> bool:
    """
    Will return True if all the docstrings are formatted correctly
    False if there is any docstring format error
    """
    error = 0
    warning = 0
    # Walk through all the folders and files in the current directory
    for root, _, files in os.walk(blocks_folder_prefix):
        # Iterate through the files
        for file in files:
            # Check if the file is a Python file and has the same name as the folder
            if file.endswith(".py") and file[:-3] == os.path.basename(root):
                # Construct the file path
                file_path = os.path.join(root, file)

                # Read the contents of the Python file
                with open(file_path, "r") as f:
                    code = f.read()

                # Parse the code
                tree = ast.parse(code)

                # Find functions in the code
                for node in ast.walk(tree):
                    if isinstance(node, ast.FunctionDef):
                        function_name = node.name

                        if function_name != os.path.basename(root):
                            # don't parse for any function that has a different
                            # name than the node file name
                            continue

                        # Extract docstring if available
                        if (
                            node.body
                            and isinstance(node.body[0], ast.Expr)
                            and isinstance(node.body[0].value, ast.Str)
                        ):
                            docstring = node.body[0].value.s

                            # Process the docstring using docstring_parser
                            parsed_docstring = parse(docstring)

                            if not parsed_docstring.short_description:
                                print(
                                    f"{err_string} short_description not found for {function_name}"
                                )
                                error += 1

                            if not parsed_docstring.long_description:
                                # it is okay to not have a long description
                                parsed_docstring.long_description = ""

                            if not parsed_docstring.params:
                                print(
                                    f"{err_string} 'Parameters' not found for {function_name}"
                                )
                                error += 1

                            if not parsed_docstring.many_returns:
                                print(
                                    f"{warn_string} 'Returns' not found for {function_name}"
                                )
                                warning += 1

                            # Build the JSON data
                            json_data = {
                                "long_description": parsed_docstring.long_description,
                                "short_description": parsed_docstring.short_description,
                                "parameters": [
                                    {
                                        "name": param.arg_name,
                                        "type": param.type_name,
                                        "description": param.description,
                                    }
                                    for param in parsed_docstring.params
                                ],
                                "returns": [
                                    {
                                        "name": rtn.return_name,
                                        "type": rtn.type_name,
                                        "description": rtn.description,
                                    }
                                    for rtn in parsed_docstring.many_returns
                                ],
                            }

                            # Write the data to a JSON file in the same directory
                            output_file_path = os.path.join(root, "docstring.json")
                            with open(output_file_path, "w") as output_file:
                                json.dump(json_data, output_file, indent=2)

                                # sys.exit(0)
                        else:
                            print(
                                f"{err_string} Docstring not found for {function_name}"
                            )
                            error += 1

    print(
        f"Summary: found {error} [bold red]ERRORS[/bold red] and {warning} [bold yellow]WARNINGS[/bold yellow] with docstring formatting"
    )

    if error > 0:
        return False
    return True
