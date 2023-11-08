---
title: Create a Flojoy Block
description: Create your own Flojoy Block using Python.
slug: "contribution/blocks/custom-flojoy-block"
---

To create a new Flojoy Block, you can use our CLI to generate the boilerplate
code for you!

First, we recommend you to have [just](https://just.systems/) installed, this
allows you to type `just add BLOCK_NAME` anywhere in the blocks repository,
instead of typing out the full command (`poetry run fjblocks.py add BLOCK_NAME`)

Once you have **just** installed, head to anywhere in the blocks folder and
run `just add BLOCK_NAME`.

For example, if I am in the `blocks/AI_ML/CLASSIFICATION/` folder, I can run
`just add MY_NEW_ML_BLOCK` and my new block will be located at
`blocks/AI_ML/CLASSIFICATION/MY_NEW_ML_BLOCK/MY_NEW_ML_BLOCK.py`.
