warn_string = "[bold yellow]Warning![/bold yellow]"
err_string = "[bold red]Error![/bold red]"

docs_folder_prefix = "docs/src/content/docs/blocks/"
blocks_folder_prefix = "blocks/"

block_template = """\
from flojoy import flojoy, DataContainer


@flojoy
def {block_name}(
    default: DataContainer,
) -> DataContainer:
    pass
"""
