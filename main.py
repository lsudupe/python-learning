from DNAtoolkit import *
import random
from Structures import *


#join y random para crear un string de nucleotidos aleatorios
randDNAStr = ''.join([random.choice(Nucleotides)
                        for nuc in range(50)])

DNAStr = validateSeq(randDNAStr)

print(f'\nSequence: {DNAStr}\n')
print(f'[1] + Sequence Length: {len(DNAStr)}\n')
print(f'[2] + Nucleotide Frequency: {countNucFrequency(DNAStr)}\n')
print(f'[3] + DNA/RNA Transcription: {transcription(DNAStr)}\n')
print(f"[4] + DNA String + Reverse Complement:\n5' {DNAStr} 3'")
print(f"   {''.join(['|' for c in range(len(DNAStr))])}")
print(f"3' {reverse_complement(DNAStr)[::-1]} 5' [Complement]")
print(f"3' {reverse_complement(DNAStr)} 3' [Rev. Complement]\n")
print(f"[5] + GC content: {GC_content(DNAStr)}%\n")
print(f"[6] + CG content in Subsection k=5: {gc_content_subsec(DNAStr, k=5)}\n")






