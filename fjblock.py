import os
import sys

import typer
from rich import print

from cli.cmd import add, sync
from cli.constants import blocks_folder_prefix, docs_folder_prefix, err_string
from cli.logging import err_console
from cli.state import state

app = typer.Typer()
app.command()(add.add)
app.command()(sync.sync)


@app.callback()
def main(verbose: bool = False):
    if verbose:
        print("Verbose mode is on!")
        state["verbose"] = True


if __name__ == "__main__":
    # this is to make sure we are running the cli in the right directory
    required_folders = [docs_folder_prefix, blocks_folder_prefix]
    if not all([os.path.isdir(folder) for folder in required_folders]):
        err_console.print(
            f"{err_string} fjblock.py must be run at a directory where the following folders are present: {required_folders}"
        )
        sys.exit(1)

    app()
