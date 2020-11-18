#!/usr/bin/env python3

"""
Author: Yuchen Huang
Script to solve problem 9
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
        # extract the DNA and the motif
        result = []
        for line in f:
            linestrip = line.strip()
            result.append(linestrip)
        DNA = result[0]
        motif = result[1]
        return DNA, motif

def find_motif(DNA, motif):
    """
    Find the position of the motifs in a DNA string
    :param DNA: a string of DNA
    :param motif: a string of motif
    :return: a list of the position of the motif that is found in the DNA
    """
    # appends the positions in the position list
    position = []
    for i in range(len(DNA) - len(motif)):
        if DNA[i:i + len(motif)] == motif:
            position.append(i+1)
    return position

def write_results(filename, result):
    """
    Write the result into the filename
    :param filename: path to write the file (or filename without a path)
    :param result: the result of rosalind
    :return: the file written in the specified path (or filename)
    """
    with open(filename, "w") as f:
        for p in result:
            f.write(f"{p} ")

if __name__ == "__main__":
    # specify the filename and resultfile name
    filename = argv[1]
    writefilepath = argv[2]
    # parse the values in the file
    DNA, motif = parse_input(filename)
    # find the motif positions in the DNA
    position = find_motif(DNA, motif)
    for p in position:
        print(p, end=" ")
    # writing the result to a writefilepath
    write_results(writefilepath, position)