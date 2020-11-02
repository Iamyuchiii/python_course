#!/usr/bin/env python3

"""
Author: Yuchen Huang
Script to solve problem 3
"""

# import statements
from sys import argv

def parse_input(filename):
    """
    Parsing the content into a string
    :param filename: the path to the file
    :return: a and b value extracted from the file
    """
    with open(filename, "r") as f:
        # the first line is the DNA
        DNA = f.readline()
        return DNA

def transcription(DNA):
    """
    :param DNA: a string of DNA
    :return: a string of RNA transcribed from input DNA
    """
    RNA = DNA.replace("T", "U")
    return RNA

def write_results(filename, result):
    """
    Write the result into the filename
    :param filename: path to write the file (or filename without a path)
    :param result: the result of rosalind
    :return: the file written in the specified path (or filename)
    """
    with open(filename, "w") as f:
        f.write(result)

if __name__ == "__main__":
    # specify the filename and resultfile name
    filename = argv[1]
    writefilepath = argv[2]
    # parse the values in the file
    DNA = parse_input(filename)
    # transcripting the DNA to RNA
    RNA = transcription(DNA)
    print (RNA)
    # writing the result to a writefilepath
    write_results(writefilepath, RNA)
