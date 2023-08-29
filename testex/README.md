# Testex Python Script (Test Exercise)


Runs the tests for an [Exercism Python track](https://exercism.org/tracks/python) exercise, effectively running:

    ```
    python3 -m pytest -o marker=task -v <exercise_name_test.py>
    ```

## Installation

After cloning or downloading the `testex.py` file, in MacOS, copy `testex.py` to `/usr/local/bin` and enter your password. Make it executable by running `chmod +x /usr/local/bin/testx.py` from your CLI or Terminal.

## Running the command

Navigate to the exercise directory of the exercise you wish to run tests for and run `testex.py`:

```zsh
exercise-name $ testex.py
```

This will run the included test file on the exercise and return the results.

To run it without the `.py` extension, create and/or edit your `.zshrc` file (assuming your running it in the default macOS zsh shell) and add at the end of the file `alias testex='/usr/local/bin/testex.py'`:

```zsh
$ sudo nano ~/.zshrc
```

Once in the nano text editor type or paste:

```
alias testex='/usr/local/bin/testex.py'
```

Hit `Control-X` to exit and `Y` then `Enter` to save the file. The terminal or CLI may need to be restarted for the changes to take effect. Afterwards you should be able to run the command using `testex`

```zsh
exercise-name $ testex
```
