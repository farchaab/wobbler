import sys
from Bio import Align

if len(sys.argv) != 2:
    exit("Usage: wobbler.py <alingment>")

# wobble letters from https://www.biosearchtech.com/support/faqs/custom-oligonucleotides-modifications/what-are-wobbles
wobble = {
    "A+G": "R",
    "A+T": "W",
    "A+C": "M",
    "C+T": "Y",
    "C+G": "S",
    "G+T": "K",
    "C+G+T": "B",
    "A+G+T": "D",
    "A+C+T": "H",
    "A+C+G": "V",
    "A+C+G+T": "N",
}

alignments = Align.read(sys.argv[1], "fasta")


# Get unique nucleotides at each alignment position
def main():
    l = {}
    for i in range(alignments.shape[1]):
        tmp = []
        for record in alignments:
            if record[i] != "-":  # Ignore gaps
                tmp.append(record[i].upper())
                tmp = sorted(set(tmp))
                l[i] = "+".join(tmp)

    return "".join([wobble[val] if "+" in val else val for val in l.values()])
