---
title: Flojoy Blocks Section
---

Looking to add/update the docs page for the Flojoy Block you made? Here is a simple
breakdown of the repo structure and the steps you need to take.

All the Flojoy Blocks documentation is located in the `docs/src/content/docs/blocks/`
of this repo. **Note that in this directory, all the files except `overview.md`
are auto-generated, and nobody should edit them manually.**

If you wish to edit the overview page for one of the block category, you can
edit the `overview.md` file directly.

However, if you are trying to add a doc page for the block you made, or edit the
doc page for a specific block, you must do that in the `blocks/` directory. You
can find more instructions below.

Each block's documentation page is made of the following components:

##### 1. A prettified docstring display for this block

To update this component, you need to update the docstring on the block's Python
code itself, and then run `poetry run python3 fjblock.py sync` to regenerate the
docs page. This will auto regenerate the docstring for you.

##### 2. The Python source code for the block

Same as point above, just edit the block's Python code directly and run
`poetry run python3 fjblock.py sync`.

##### 3. An example Flojoy app using this block

To add/update the example app, you will have to add an `app.json` file which
sits in the same folder at the block's Python code. Or simply update the
existing `app.json` file to be your updated Flojoy app. You do not need to run
the sync command in this case.

##### 4. A breakdown of this example app

Same idea as before, you can add an `example.md` file in the same folder as the
block's Python code. Or simply update the existing `example.md` file. Run
`poetry run python3 fjblock.py sync` once you are done!

Happy contributing, we cannot wait to see the Flojoy Block you made!
