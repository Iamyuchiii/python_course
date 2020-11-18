#!/usr/bin/env python3

"""
Author: Yuchen Huang
Script to solve problem 10
"""

from sys import argv

def parse_fasta(filename):
    """
    Parsing the content into a string
    :param filename: the path to the file
    :return: a and b value extracted from the file
    """
    # parsing the fasta file into a
    with open(filename, "r") as f:
        fasta = {}
        temp = []
        for line in f:
            if line.startswith(">"):
                header = line[1:].strip()
                fasta[header] = ""
            else:
                sequence = line.strip()
                temp.append(sequence)
                fasta[header] = "".join(temp)
        return fasta[header]


def reverse_complement(DNA):
    """
    Computing the reverse DNA from the input DNA
    :param DNA: a string of DNA
    :return: the reverse complement of the DNA (3` - 5`)
    """
    DNA_complement = {"A" : "T", "C" : "G", "T" : "A", "G" : "C"}
    complement = ""
    for n in DNA:
        # for each n in DNA, the complement is taken out and added to the variable complement
        complement = DNA_complement[n] + complement # this adds the strings in reverse
    return complement

def restriction_site(DNA, lowerange, upperange):
    """
    finds the possible restriction sites and gives its position
    :param DNA: a string of DNA
    :param lowerange: the lower range of the k-mer string
    :param upperange: the upper range of the k-mer string
    :return: the position and the length of the restriction site in a dictionary
    """
    possible_position = {}
    # get the len of the DNA
    for i in range(len(DNA)):
        for j in range(lowerange, upperange+1):
            if i+j > len(DNA):
                continue
            # get all possible kmer in the DNA
            p_DNA = DNA[i:i+j]
            r_pDNA = reverse_complement(p_DNA)
            # chose all the possible kmer which fits the criteria
            if p_DNA == r_pDNA:
                possible_position[i+1] = len(p_DNA)
    return possible_position

def write_results(filename, result):
    """
    Write the result into the filename
    :param filename: path to write the file (or filename without a path)
    :param result: the result of rosalind
    :return: the file written in the specified path (or filename)
    """
    with open(filename, "w") as f:
        for k, v in result.items():
            print(k, v, file = f)

if __name__ == "__main__":
    filename = argv[1]
    writefilepath = argv[2]
    # parse the fasta file and get the sequence
    sequence = parse_fasta(filename)
    # find the position of restriction sites
    result = restriction_site(sequence,4,12)
    # printing the result
    for k, v in result.items():
        print(k, v)
    # writing the result into a file
    write_results(writefilepath, result)