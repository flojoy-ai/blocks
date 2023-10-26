WARN_STRING = "[bold yellow]Warning![/bold yellow]"
ERR_STRING = "[bold red]Error![/bold red]"

DOCS_FOLDER = "docs/src/content/docs/blocks/"
BLOCKS_FOLDER = "blocks/"

BLOCK_TEMPLATE = """\
from flojoy import flojoy, DataContainer, OrderedPair, Vector
from typing import Optional, Literal


@flojoy
def {block_name}(
    default: DataContainer,
) -> DataContainer:
    pass
"""
