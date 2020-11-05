#!/usr/bin/env python3

"""
Author: Yuchen Huang
Script to solve problem 8
"""

# import statements
from sys import argv
import regex as re

# ATG([ATCG]{3})*?(TAG|TGA|TAA)

def parse_input(filename):
    """
    Parsing the content into a string
    :param filename: the path to the file
    :return: a and b value extracted from the file
    """
    with open(filename, "r") as f:
        # read the whole file and splits the content with ">"
        file_content = f.read()
        entries = file_content.split(">")[1:]
        # create a empty dictionary
        sequences_dict = {}
        for ent in entries:
            # selected the label (header) and seqeuence. x is the \n
            label, x, sequence = ent.partition("\n")
            # replace the rest of the \n in the sequence
            sequences_dict[label] = sequence.replace("\n", "")
        return sequences_dict[label]


DNA_CODON_TABLE = {
    'TTT': 'F',     'CTT': 'L',     'ATT': 'I',     'GTT': 'V',
    'TTC': 'F',     'CTC': 'L',     'ATC': 'I',     'GTC': 'V',
    'TTA': 'L',     'CTA': 'L',     'ATA': 'I',     'GTA': 'V',
    'TTG': 'L',     'CTG': 'L',     'ATG': 'M',     'GTG': 'V',
    'TCT': 'S',     'CCT': 'P',     'ACT': 'T',     'GCT': 'A',
    'TCC': 'S',     'CCC': 'P',     'ACC': 'T',     'GCC': 'A',
    'TCA': 'S',     'CCA': 'P',     'ACA': 'T',     'GCA': 'A',
    'TCG': 'S',     'CCG': 'P',     'ACG': 'T',     'GCG': 'A',
    'TAT': 'Y',     'CAT': 'H',     'AAT': 'N',     'GAT': 'D',
    'TAC': 'Y',     'CAC': 'H',     'AAC': 'N',     'GAC': 'D',
    'TAA': 'Stop',  'CAA': 'Q',     'AAA': 'K',     'GAA': 'E',
    'TAG': 'Stop',  'CAG': 'Q',     'AAG': 'K',     'GAG': 'E',
    'TGT': 'C',     'CGT': 'R',     'AGT': 'S',     'GGT': 'G',
    'TGC': 'C',     'CGC': 'R',     'AGC': 'S',     'GGC': 'G',
    'TGA': 'Stop',  'CGA': 'R',     'AGA': 'R',     'GGA': 'G',
    'TGG': 'W',     'CGG': 'R',     'AGG': 'R',     'GGG': 'G',
    'SEP':'SEP'
}

"""
Without using regex
"""
def complement_DNA(DNA):
    """
    reverse the input DNA into a complement strand
    :param DNA: a string of DNA
    :return: the complement of the DNA
    """
    # transform DNA into complement DNA, provide a DNA string.
    DNA_complement = {"A": "T", "C": "G", "T": "A", "G": "C"}
    complement_DNA = []

    for n in DNA: # looping over each nucleotide in DNA
        for nucleotide, complement in DNA_complement.items(): # looping over each key and value in DNA_complement
            if n == nucleotide: # if nucleotide is the same with key in DNA_complement, append the value in the list complement_DNA
                complement_DNA.append(complement)
    complement_DNA = "".join(complement_DNA[::-1]) # joining the list into a string
    return complement_DNA

def translate_codon(codon):
    """
    translate the DNA into AA using a dictionary table
    :param codon: three letters DNA
    :return: AA for the three DNA letters
    """
    # translate each codon (three pair nucleotide) into protein, provide three pair nucleotide
    protein = ""
    for c, p in DNA_CODON_TABLE.items(): # loop over codon and protein in DNA_CODON_TABLE
        if len(codon) == 3 and codon == c: # if codon is three pair and codon matches the codon in codon_table, assign key in de string protein.
            protein = DNA_CODON_TABLE[codon]
    return protein

def find_orf(DNA):
    """
    finds the orfs in the DNA string
    :param DNA: a string of DNA
    :return: all possible orfs
    """
    # finds_orf in DNA, provide DNA and complement_DNA
    indices = []
    orfs = []

    for n in range(len(DNA)): # loop over each the totale length of DNA
        protein = translate_codon(DNA[n:n+3]) # Translate all possible codon in the DNA
        if protein == "M": # if the codon matches M, append the index where the codon M in the DNA string occurs
            indices.append(n)

    for i in indices: # loop over all possible indices in indices list
        possible_protein = ""
        No_stop = True
        for n in range(i,len(DNA),3): # loop over all possible codon beginning from start codon
            protein = translate_codon(DNA[n:n+3]) # Translate all the codons
            if protein == "Stop": # if there is a stop codon, finish the loop
                No_stop = False # change No_stop to false when stop codon is found
                break # finish the loop

            possible_protein += protein # append all the possible translated proteins
        if No_stop == False: # append proteins with start and stop codon
            orfs.append(possible_protein)
    return orfs

"""
Using regex
"""

def find_orfs(DNA):
    list_orf = []
    orf = re.finditer(r"ATG([ATCG]{3})*?(TAG|TGA|TAA)", DNA, overlapped = True)
    for i in orf:
        seq = i.group()
        result = translate_codon2(seq)
        list_orf.append(result)
    return list_orf

def translate_codon2 (DNA):
    # loop though the 3 positions in RNA to generated a codon
    protein = ""
    for position_codon in range(0, len(DNA), 3):
        # string slicing to get the 3 pairs strings
        codon = DNA_CODON_TABLE[DNA[position_codon:position_codon + 3]]
        # if the codon value is not STOP then the function keeps appending the AA to the list protein
        if codon != "Stop":
            protein += codon
    return protein


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
    DNA = parse_input(filename)
    # reverse DNA
    DNA_compliment = complement_DNA(DNA)
    # """
    # regex way
    # """
    # # find all possible orfs in the DNA/DNA_compliment
    # r_orfs = find_orfs(DNA)
    # r_orfs2 = find_orfs(DNA_compliment)
    # rfinal_result = "\n".join(set(r_orfs + r_orfs2))
    # print(rfinal_result)

    """
    normal way
    """
    # find orfs in both reverse strand and forward strand
    result1 = find_orf(DNA)
    result2 = find_orf(DNA_compliment)
    final_result = "\n".join(set(result1+result2))
    print(final_result)
    # write results to a file
    write_results(writefilepath, final_result)

