# Openex Python Script (Open Exercise)

![Static Badge](https://img.shields.io/badge/my_first_script-blue?style=flat)


This is a simple script that opens the following files from an [Exercism Python track](https://exercism.org/tracks/python) exercise:

    `README.md`
    `exercise_name.py`
    `exercise_name_test.py`

## Installation

After cloning or downloading the `openex.py` file, in MacOS, move `openex.py` to `/usr/local/bin` and enter your password. Make it executable by running `chmod +x /usr/local/bin/openex.py` from your CLI or Terminal.

## Running the command

After downloading the Exercism exercise, navigate to the exercise directory in your CLI or IDE terminal and run `openex.py`:

```zsh
exercise-name $ openex.py
```

This will open the aforementioned files in the default IDE or text editor on your machine. (i.e. VS Code, PyCharm, etc)

To run it without the `.py` extension, create and/or edit your `.zshrc` file (assuming your running it in the default macOS zsh shell) and add at the end of the file `alias openex='/usr/local/bin/openex.py'`:

```zsh
$ sudo nano ~/.zshrc
```

Once in the nano text editor type or paste:

```
alias openex='/usr/local/bin/openex.py'
```

Hit `Control-X` to exit and `Y` then `Enter` to save the file. The terminal or CLI may need to be restarted for the changes to take effect. Afterwards you should be able to run the command using `openex`

```zsh
exercise-name $ openex
```
