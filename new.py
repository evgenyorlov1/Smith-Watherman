__author__ = 'adm'
import Bio.pairwise2
from Bio.SubsMat import MatrixInfo

#strG = str(raw_input("Genome sequence: "))
#strR = str(raw_input("Read sequence: "))
#strG = strG.upper()
#strR = strR.upper()
#print "Your genome ref input : " +strG
#print "Your read ref input   : " +strR

blosum = MatrixInfo.blosum62
pair = ('A', 'A')
print blosum[pair]

def score_matrix(pair, matrix):
    '''return blosum matrix score'''
    if pair not in matrix:
        return matrix[(tuple(reversed(pair)))]
    else:
        return matrix[pair]

def make_matrix(sizex, sizey):
    '''builds matrix'''
    return[[0]*sizey for i in xrange(sizex)]

def local_align(x, y, score):
    A = make_matrix(len(x)+1, len(y)+1)

def main():
    pass

if __name__ == "__main__":
    main()

#A = make_matrix(len(strG) + 1, len(strR) + 1)
