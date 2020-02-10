import sys
import numpy as np

word1=sys.argv[1]
word2=sys.argv[2]

def create_matrix(word1, word2, m, n):
    lmatrix = np.arange((m+1)*(n+1)).reshape(m+1,n+1)
    for i in range(m+1):
        lmatrix[i][0]=i
    for j in range(n+1):
        lmatrix[0][j]=j
    return lmatrix

#lmatrix = create_matrix(word1,word2)
#print(lmatrix)


def levenshtein(word1, word2):
    m = len(word1)
    n = len(word2)
    lmatrix = create_matrix(word1,word2,m,n)
    for i in range(1,lx):
        for j in range(1,ly):
            if min(i,j) == 0:
                lmatrix[i][j]=max(i,j)
            else:
                factor = 1 if word1==word2 else 0
                lmatrix[i][j]=min(lmatrix[i-1,j]+1,lmatrix[i][j-1]+1,lmatrix[i-1,j-1]+factor)
    return lmatrix    


res_matrix = levenshtein(word1,word2)
#print(res_matrix.shape, len(word1)+1, len(word2)+1)
distance = res_matrix[len(word1)][len(word2)]
print(distance)
