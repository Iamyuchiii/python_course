with open("D:/Pycharm_project/Master_bioinformatics/Rosalind/workfiles/rosalind_revc.txt", "r") as inputf:
    for line in inputf:
        DNA = line
        DNA = DNA.replace("\n","")

def reverse_complement(DNA):
    DNA_complement = {"A" : "T", "C" : "G", "T" : "A", "G" : "C"}
    complement = ""
    for n in DNA:
        complement = DNA_complement[n] + complement
    return complement

with open("D:/Pycharm_project/Master_bioinformatics/Rosalind/workfiles/rosalindans.txt", "w") as ansf:
    print (reverse_complement(DNA), file = ansf)