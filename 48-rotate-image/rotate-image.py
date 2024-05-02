class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # we will replicate the matrix such that the replicate will contain the original values
        clone=[]

        for row in matrix:
            reprow=[]
            for element in row :
                reprow.append(element)
            clone .append(reprow)
        #print the cloned matrix
        print(clone)
        rows=len(matrix)
        rows=rows-1
        print("the row number is ")
        print(rows)
        k=rows
        i=0
        j=0
        #now go over the clone and make changes in the real matrix
        for i in range (rows+1):
            rev=rows-i
            for j in range (rows+1):
                print(i, " ", j, " ", k, "\n")
                matrix[i][j]=clone[k][i]
                k-=1
            k=rows



# class Solution:



#      def rotate(self, matrix: List[List[int]]) -> None:
#         n = len(matrix)
#         # Step 1: Transpose the matrix
#         for i in range(n):
#             for j in range(i + 1, n):
#                 matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

#         # Step 2: Reverse each row
#         for i in range(n):
#             matrix[i].reverse()