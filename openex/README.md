# Openex Python Script (Open Exercise)

![Static Badge](https://img.shields.io/badge/my_first_script-blue?style=flat)


This is a simple script that opens the following files from an [Exercism Python track](https://exercism.org/tracks/python) exercise:

    `README.md`
    `exercise_name.py`
    `exercise_name_test.py`

## Installation

After cloning or downloading the `openex.py` file, in MacOS, move `openex.py` to `/usr/local/bin` and enter your password. Make it executable by running `chmod +x /usr/local/bin/openex.py` from your CLI or Terminal.

## Running the command

After downloading the Exercism exercise, navigate to the exercise directory in your CLI or IDE terminal and run `openex`:

```bash
exercise-name $ openex
```

This will open the aforementioned files in the default IDE or text editor on your machine. (i.e. VS Code, PyCharm, etc)

## Things to be aware of: Edge cases

This script will return an error with a message that the file was not found if run in an exercise directory where the Python filename doesn't match the directory name, such as a learning exercise. (i.e. For the exercise *Card Games* the directory name is `card-games` but the filename is `lists.py` and test filename is `lists_test.py`)