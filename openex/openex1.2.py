#!/usr/bin/env python3

# Above line enables openex to be globally executed (from any directory)
# by setting the environment to Python3

"""Opens Exercism Python track README.md, exercise.py and exercise_test.py 
files when the exercise path is set to the current directory.
"""

from os         import getcwd, walk
from sys        import exit
from subprocess import run

def main():
    
    file_suffix = "_test.py"
    directory = getcwd()
    exercise = ''
    
    # Search directory for file
    for path, dirs, files in walk(directory):
        for file in files:
            if file_suffix in file:
                exercise = file.removesuffix(file_suffix)
    
    if exercise == '':
        exit('Error: File not found.')
    
    # Set command and files
    command = "open"
    readme_file = [command, "README.md"]
    exercise_file = [command, f"{exercise}.py"]
    test_file = [command, f"{exercise}_test.py"]

    # Run command subprocess and set it to check for errors
    run(readme_file, check=True)
    run(exercise_file, check=True)
    run(test_file, check=True)


if __name__ == "__main__":
    main()