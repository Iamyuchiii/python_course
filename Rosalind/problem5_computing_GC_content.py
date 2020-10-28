#!/usr/bin/env python3

"""
Author: Yuchen Huang
Script to solve problem 5
"""

# import statements
from sys import argv

def convert_fasta_to_dic (filename):
    """
    convert de fasta file into a dictionary
    :param filename: the path to the file or the file name
    :return: a dictionary
    """
    with open(filename, "r") as f:
        header = []
        samples = []
        sample = ""
        for line in f:
            # adds the header to the header list
            if line.startswith(">"):
                headerline = line.strip()
                header.append(headerline[1:])
                samples.append(sample)
                sample = ""
            # adds the sequence to the samples list
            else:
                sample += line.strip()
        samples.append(sample)

        # make a empty dictionary
        DNA_dict = {}
        # loop through 2 list header and samples and add them as key and value pairs in dic
        for h, s in zip(header,samples[1:]):
            DNA_dict[h] = s

        return DNA_dict

def GC_content(DNA):
    """
    Counts the GC in DNA sequence and calculates the GC content in the DNA string
    :param DNA: string of DNA
    :return: the GC content
    """
    # counts the G and C in the the DNA string
    G = DNA.count("G")
    C = DNA.count("C")
    # calculates the GC content in the DNA
    gc_content = (G + C) / len(DNA)
    return gc_content * 100

def comparing_GC(DNA_dic):
    """
    Calculates all GC_concent in the dictionary and returns the highest GC value with the header name
    :param DNA_dic: A dictionary that is convertated from a FASTA file
    :return: The highest GC value with its header name
    """
    compare = []
    for keys, value in DNA_dic.items():
        gc_content = GC_content(value)
        compare.append(gc_content)
    highest_value = max(compare)
    index_highest = compare.index(highest_value)
    header = list(DNA_dic)
    return header[index_highest], highest_value

def write_result(filename, result):
    """
    :param filename: the path with filename (or the filename) that you wanted the file to be called
    :param result: the result obtained comparing_gc
    :return: a txt file containing the reuslt called the filename spefified in the param.
    """
    with open(filename, "w") as f:
        header, highest_value = result
        f.write(f"{header}\n{highest_value}")

if __name__ == "__main__":
    # extract the filename
    filename = argv[1]
    writefilepath = argv[2]
    # convert fasta to dictonary
    DNA_dictionary = convert_fasta_to_dic(filename)
    # calculate gc value and select the higest GC value
    result = comparing_GC(DNA_dictionary)
    header, highest_value = comparing_GC(DNA_dictionary)
    # printing the result
    print(header)
    print(highest_value)
    # writing the result into the path specified in writefilepath
    write_result(writefilepath, result)