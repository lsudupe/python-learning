# DNA toolkit
import collections
from Structures import *

#Check the secuence to make sure it is a DNA string
def validateSeq(dna_seq):
    tmpseq = dna_seq.upper()
    for nuc in tmpseq:
        if nuc not in Nucleotides:
            return False
        return tmpseq


def countNucFrequency(seq):
    tmpFreqDict = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    for nuc in seq:
        tmpFreqDict[nuc] += 1
    return tmpFreqDict
    

def transcription(seq):
    '''DNA > RNA transcriptions : Replacing Thimine with Uracile'''
    return seq.replace('T', 'U')


def reverse_complement(seq):
    return ''.join([DNA_ReverseComplement[nuc] for nuc in seq])[::-1]


def GC_content(seq):
    return round(((seq.count('G') + seq.count('C'))*100)/len(seq), 4)


def gc_content_subsec(seq, k=20):
    '''GC Content in a DNA/RNA sub-sequence length k. k=20 by default'''
    res = []
    for i in range(0, len(seq) - k + 1, k):
        subseq = seq[i:i + k]
        res.append(GC_content(subseq))
    return res

def translate_seq(self, init_pos=0):
    """Translates a DNA sequence into an aminoacid sequence"""
    if self.seq_type == "DNA":
        return [DNA_Codons[self.seq[pos:pos + 3]] for pos in range(init_pos, len(self.seq) - 2, 3)]
    elif self.seq_type == "RNA":
        return [RNA_Codons[self.seq[pos:pos + 3]] for pos in range(init_pos, len(self.seq) - 2, 3)]
