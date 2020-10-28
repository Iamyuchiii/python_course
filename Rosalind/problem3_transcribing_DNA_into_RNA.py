with open("D:/Pycharm_project/Master_bioinformatics/Rosalind/workfiles/rosalind_rna.txt", "r") as inputf:
    for line in inputf:
        DNA = line

def transcription(DNA):
    """
    :param DNA: a string of DNA
    :return: a string of RNA transcribed from input DNA
    """
    RNA = DNA.replace("T", "U")
    return RNA

with open("D:/Pycharm_project/Master_bioinformatics/Rosalind/workfiles/rosalindans.txt", "w") as ansf:
    print (transcription(DNA), file = ansf)