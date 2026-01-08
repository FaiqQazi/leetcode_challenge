class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        matrix=[[0]*(len(word1)+1) for _ in range(len(word2)+1)]
        for i in range (len(word2)+1):
            matrix[i][len(word1)]=len(word2)-i
        for j in range(len(word1)+1):
            matrix[len(word2)][j]=len(word1)-j
        for i in range(len(word2)-1,-1,-1):
            for j in range (len(word1)-1,-1,-1):
                if word2[i]==word1[j]:
                    matrix[i][j]=matrix[i+1][j+1]
                else:
                    matrix[i][j] = 1 + min(
                        matrix[i + 1][j],     # delete
                        matrix[i][j + 1],     # insert
                        matrix[i + 1][j + 1]  # replace
                    )       
        return matrix[0][0]