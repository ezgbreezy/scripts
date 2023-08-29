#!/usr/bin/env python3

"""Runs Exercism exercise tests.
"""

from os         import getcwd, walk
from subprocess import call
from sys        import argv

def main():
   
    file_suffix = "_test.py"
    directory = getcwd()
    exercise = ''

    for file in walk(directory):
        if file_suffix in file:
            exercise = file

    if '-' in exercise:
        exercise = exercise.replace('-','_')
    test = f'python3 -m pytest -o marker=task -v {exercise}'.split()
    call(test)

if __name__ == "__main__":
    main()