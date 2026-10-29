# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

A personal Python learning repo (not an application): sequentially numbered Jupyter notebooks working through Python fundamentals, plus a few standalone homework/practice scripts. There is no build system, package manifest, test suite, or linter.

## Layout

- `01-…` to `18-…` `.ipynb` notebooks follow a course progression: numbers, strings, variables, lists, tuples, dicts, sets, comparison operators, control flow, loops, comprehensions, functions, args/kwargs, scope, functional programming, unpacking/decorators/exceptions, OOP. Filenames are inconsistent (e.g. `09 -if, elif, and else Statements.ipynb` contains spaces), so quote paths in shell commands.
- `11.1-Problem.ipynb` is a side exercise for the while-loops notebook.
- Standalone scripts (`stringHW.py`, `10.12homework.py`, `10.12.26.py`, `12-13.py`) hold homework solutions and practice. Most code in them is commented out, and several homework prompts are written in Hebrew. Treat the commented blocks as saved exercises; don't delete or "clean up" them.

## Working here

- Run a script with `python3 <file>.py`. Many scripts call `input()`, so they are interactive.
- Open notebooks with `jupyter notebook` or `jupyter lab`. For headless execution use `jupyter nbconvert --to notebook --execute "<name>.ipynb"`.
- When editing notebooks, change cells through NotebookEdit or valid JSON edits and keep existing outputs and markdown explanations. The content is educational, so keep new examples simple and in the same explanatory style.
- Commit history is plain descriptive messages on `main`.
