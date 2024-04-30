class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        zerorow=[]
        zerocol=[]
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range (len (matrix)):
            for j in range (len(matrix[i])):
                if(matrix[i][j]==0):
                    zerorow.append(i)
                    zerocol.append(j)
        for i in range (len (matrix)):
            for j in range (len(matrix[i])):
                if(i in zerorow or j in zerocol):
                    matrix[i][j]=0



        