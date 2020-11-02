#!/usr/bin/env python3

"""
Author: Yuchen Huang
Script to solve problem 4
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
        # read the whole file and covert the RNA into a list
        RNA_string = f.read()
        return RNA_string

# DNA codon table for translation
codon_table ={
"UUU":"F", "UUC":"F", "UUA":"L", "UUG":"L",
    "UCU":"S", "UCC":"S", "UCA":"S", "UCG":"S",
    "UAU":"Y", "UAC":"Y", "UAA":"STOP", "UAG":"STOP",
    "UGU":"C", "UGC":"C", "UGA":"STOP", "UGG":"W",
    "CUU":"L", "CUC":"L", "CUA":"L", "CUG":"L",
    "CCU":"P", "CCC":"P", "CCA":"P", "CCG":"P",
    "CAU":"H", "CAC":"H", "CAA":"Q", "CAG":"Q",
    "CGU":"R", "CGC":"R", "CGA":"R", "CGG":"R",
    "AUU":"I", "AUC":"I", "AUA":"I", "AUG":"M",
    "ACU":"T", "ACC":"T", "ACA":"T", "ACG":"T",
    "AAU":"N", "AAC":"N", "AAA":"K", "AAG":"K",
    "AGU":"S", "AGC":"S", "AGA":"R", "AGG":"R",
    "GUU":"V", "GUC":"V", "GUA":"V", "GUG":"V",
    "GCU":"A", "GCC":"A", "GCA":"A", "GCG":"A",
    "GAU":"D", "GAC":"D", "GAA":"E", "GAG":"E",
    "GGU":"G", "GGC":"G", "GGA":"G", "GGG":"G",
}

def translation(RNA):
    protein = []
    for position_codon in range(0, len(RNA), 3):
        codon = codon_table[RNA[position_codon:position_codon+3]]
        if codon != "STOP":
            protein.append(codon)
    return "".join(protein)

def write_results(filename, result):
    """
    Write the result into the filename
    :param filename: path to write the file (or filename without a path)
    :param result: the result of rosalind
    :return: the file written in the specified path (or filename)
    """
    with open(filename, "w") as f:
        f.write(f"{result}")

if __name__ == "__main__":
    # specify the filename and resultfile name
    filename = argv[1]
    writefilepath = argv[2]
    # parse the values in the file
    RNA = parse_input(filename)
    # translating RNA into protein
    protein = translation(RNA)
    print(protein)
    # writing the result to a writefilepath
    write_results(writefilepath, protein)
    """
    Test area
    """
    # print(translation("AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA"))







