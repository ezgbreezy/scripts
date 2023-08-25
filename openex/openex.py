#!/usr/bin/env python3

# Above line enables openex to be globally executed (from any directory)
# by setting the environment to Python3

"""Opens Exercism Python track README.md, exercise.py and exercise_test.py 
files when the exercise path is set to the current directory.
"""

import os, subprocess

def main():
    
    # Split current directory into list,
    # assign last list item to file variable
    file = os.getcwd().split('/')[-1]

    # Replace any hyphens with underscores
    if '-' in file:
        file = file.replace('-', '_')

    # Set desired zsh command and files
    command = "open"
    md_file = [command, "README.md"]
    exercise_file = [command, f"{file}.py"]
    test_file = [command, f"{file}_test.py"]

    # Run command subprocess and set it to check for errors
    subprocess.run(md_file, check=True)
    subprocess.run(exercise_file, check=True)
    subprocess.run(test_file, check=True)


if __name__ == "__main__":
    main()