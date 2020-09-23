DNAseq = 'TAACCAGAACTAGTCGGAACGAGTGAAAGTGGCGCTGCATCATGCATCAAATGACGGCCCTACCCAGTGCGCCTGTCATGATACAGGTTTCCCACACTTCCAAGAGCATATGGTTTTAGACAGCAACCCAGGCGACATTTAAAATAACATGCCGCGGCATCAGGCCCTGATTCGTTACGAACTAGCTCAGGTATCCTCGCTGCGAGCGGAGTGCGACCGTCTCTGTTCGTGCAGATGCTCACCTATATCGAAGTCTGTTTGTCGAAGCCTAGCTTCATCTCACAGAAAATGCCTGAGTGCCACTGATGATGATCACAGTCGTAAGGGCTTCCATCCAAGAGGTTATTACGCCAGCATTCAGATGTGAGGCACGTTTCTAACGGCTTCCCTACGGGAGCGTAAACTTCTCCTTACCGGTTCTGAGTCTCACGGCGAAGGAGAGTCCGATGATCAAGAGAGAAATGCTCAGAAGCCCATGAACGTGCAGTTTATGAGATCTATGACAGTATAAGGGTTGCGCCGGAGTTATAGCGATTTCCGCACTCAGGGTGTATGCTGCCACGTCAGTTTTTTGCGCAGAGCTAATATTCCGCGTACGATTGTCATACGGCCCTGGGTCATAACAGCTCATCTGTTGAAACTATGTAGAATGCGCGTCTGTAGTACATCCATCCACCCCATGTCTATAGCTATACCTTGCACACCCCGTGCGAGCTTCGTCCAAAAATGGGGGACCTTTGCTTGACCATCGGATTAAAGCGGCGGATATATCTCCCCTGCGCAACCCGACGTCATACTAAGACTATCCCAAGCTACACGCGGGCCCGTAGCACTCCTACCG'

'''def complementDNA(DNAseq):
    nucl = 'ATCG'
    clave = 'TAGC'
    diccionario = {key:value for key, value in variable}
    complement = {key: value for key, value in zip(nucl, clave)}
    complDNA = [] #creamos un lista vacia
    for nucle in DNAseq:
        complDNA.append(complement.get(nucle, nucle))
    #podemos convertir la lista en string
    complDNA = ''.join(complDNA)
    return complDNA'''

    
#opcion mas reducida
#texto_cifrado = "".join(cifra.get(letra, letra) for letra in texto)

'''def complementDNA(DNAseq):
    nucl = 'ATCG'
    clave = 'TAGC'
    dic = {nucleotido:valor for nucleotido, valor in zip(nucl, clave)}
    cifrado = ''.join(dic.get(nucl, nucl) for nucl in DNAseq)
    return cifrado'''

#para devolver la complementaria hacia el otro lado
'''def complementDNA(DNAseq):
    complementaria = ''
    nucl = 'ATCG'
    clave = 'TAGC'
    dic = {nucleotido:valor for nucleotido, valor in zip(nucl, clave)}
    cifrado = ''.join(dic.get(nucl, nucl) for nucl in DNAseq)
    for i in range(len(cifrado)-1, -1, -1):
        complementaria += cifrado[i]
    return complementaria'''

#aun mas corta la parte inversa
def complementDNA(DNAseq):
    complementaria = ''
    nucl = 'ATCG'
    clave = 'TAGC'
    dic = {nucleotido:valor for nucleotido, valor in zip(nucl, clave)}
    cifrado = ''.join(dic.get(nucl, nucl) for nucl in DNAseq)
    return cifrado[::-1]
print(complementDNA(DNAseq))