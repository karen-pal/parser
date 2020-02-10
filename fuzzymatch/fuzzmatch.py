import sys
import numpy as np

word1=sys.argv[1].lower()
word2=sys.argv[2].lower()

def create_matrix(word1, word2, m, n):
    lmatrix = np.arange(m*n).reshape(m,n)
    for i in range(m):
        lmatrix[i][0]=i
    for j in range(n):
        lmatrix[0][j]=j
    return lmatrix


def levenshtein(word1, word2, m, n):
    lmatrix = create_matrix(word1,word2,m+1,n+1)
    #additional row and column for dynprog purposes

    for i in range(1,m+1):
        for j in range(1,n+1):
            if min(i,j) == 0:
                lmatrix[i][j]=max(i,j)
            else:
                factor = not word1[i-1]==word2[j-1]
                lmatrix[i][j]=min(lmatrix[i-1,j]+1,lmatrix[i][j-1]+1,lmatrix[i-1,j-1]+factor)
    return lmatrix    


m = len(word1) if len(word1)<4 else 4
n = len(word2) if len(word2)<4 else 4
res_matrix = levenshtein(word1, word2, m, n)
print(res_matrix)
distance = res_matrix[m][n]
print(distance)
