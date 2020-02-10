import sys
import numpy as np

word1=sys.argv[1]
word2=sys.argv[2]

def create_matrix(word1, word2, m, n):
    lmatrix = np.arange(m*n).reshape(m,n)
    for i in range(m):
        lmatrix[i][0]=i
    for j in range(n):
        lmatrix[0][j]=j
    return lmatrix

#lmatrix = create_matrix(word1,word2)
#print(lmatrix)


def levenshtein(word1, word2):

    m = len(word1)
    n = len(word2)
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


res_matrix = levenshtein(word1, word2)
print(res_matrix)
distance = res_matrix[len(word1)][len(word2)]
print(distance)
