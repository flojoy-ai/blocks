import os
import sys

import typer
from rich.console import Console

err_console = Console(stderr=True)
app = typer.Typer()

err_string = "[bold red]Error![/bold red]"


@app.command()
def add(block: str):
    print(f"Hello {block}")


if __name__ == "__main__":
    # this is to make sure we are running the cli in the right directory
    required_folders = ["blocks", "docs", "wtf"]
    if not all([os.path.isdir(folder) for folder in required_folders]):
        err_console.print(
            f"{err_string} fjblock.py must be run at a directory where the following folders are present: {required_folders}"
        )
        sys.exit(1)

    app()
