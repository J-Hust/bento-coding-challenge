# Bento For Business Coding Challenge

In this project are the solutions to the two coding exercises from Bento, separated by module.

#### one
* Takes in a path as a string, and for that directory and nested subdirectories, prints a table containing the path, filename, and size.  Results are sorted by size from largest to smallest.

#### two
* Takes in a string of lower-case letters and prints the string with repeating characters replaced by the number of times the character is repeated.  For example:
    * `'abbcddde' ----> 'ab2cd3e'`

## Requirements

* `python 3`

## Usage

Two modules are present in the `src` directory - one for each coding exercise.  A command-line interface is provided:

```bash
python3 -m src.app --module one --path 'path/to/be/displayed'
```

```bash
python3 -m src.app --module two --string 'abcdefgh'
```