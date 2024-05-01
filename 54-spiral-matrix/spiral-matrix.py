
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        array=[]
        boolval=False
        rowbol=False
        colbol=False
        finalbol=False
        rows = len(matrix)
        cols = len(matrix[0]) if matrix else 0  # Assuming the matrix is non-empty

        # Create a boolean matrix with the same size as the given matrix, all values set to False
        bool_matrix = [[False for _ in range(cols)] for _ in range(rows)]
        i=0
        j=0
        revi=rows - 1
        revj=cols - 1
        
        while i <= revi and j <= revj:
            if boolval == False and rowbol == False:
                # Iterate over each element in the row
                for z in range(cols):
                    if not bool_matrix[i][z]:
                        array.append(matrix[i][z])  # Append current element to the result array
                        bool_matrix[i][z] = True  # Mark the corresponding cell as visited
                boolval = True
                rowbol = True
                i += 1

            elif not boolval and rowbol:
                
                for y in range(cols - 1, -1, -1):  # Iterate over the range of indices in reverse order
                    if not bool_matrix[revi][y]:
                        array.append(matrix[revi][y])  # Append current element to the result array
                        bool_matrix[revi][y] = True  # Mark the corresponding cell as visited
                boolval = True
                rowbol = False
                revi -= 1

            elif boolval == True and colbol == False:
                # Iterate over each row in the column
                for m in range(rows):
                    if not bool_matrix[m][revj]:  
                        # Check if the current cell is not visited
                        array.append(matrix[m][revj])  # Append the element to the result array
                        bool_matrix[m][revj] = True  # Mark the corresponding cell as visited
                boolval = False
                colbol = True
                revj -= 1

            elif boolval == True and colbol == True:
                # Iterate over each row in the column in reverse order
                for m in reversed(range(rows)):
                    if not bool_matrix[m][j]:  # Check if the current cell is not visited
                        array.append(matrix[m][j])  # Append the element to the result array
                        bool_matrix[m][j] = True  # Mark the corresponding cell as visited
                boolval = False
                colbol = False
                j += 1
            
        return array
