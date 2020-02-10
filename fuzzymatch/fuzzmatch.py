import sys
import numpy as np

word1=sys.argv[1]
word2=sys.argv[2]

def create_matr(word1,word2):
    m = len(word1)
    n = len(word2)
    matrix = np.arange().reshape(m+1,n+1)
    for i in range(m):
        matrix[][]=i
    for j in range(n):
        matrix[][]=j
    return matrix

def levenshtein(word1, word2,i,j):
    matrix = creat_matr(word1,word2)
    if min(i,j) == 0:
        return max(i,j)

res = levenshtein(word1,word2, len(word1)+1, len(word2)+1)
