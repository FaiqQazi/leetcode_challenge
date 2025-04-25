# class Solution:
#     def minPathSum(self, grid: List[List[int]]) -> int:
#         if (len(grid) - 1) == 0 and (len(grid[0]) - 1) == 0:
#             return grid[0][0]
#         print(grid)
#         #make a 3d array containing the values that each recieves from left and right
#         rows = len(grid)
#         cols = len(grid[0])

#         # Create a 3D list with same 2D shape as grid, and third dimension = 2
#         arr = [[[0, 0] for _ in range(cols)] for _ in range(rows)]
#         for i in range(len(grid)):
#             for j in range(len(grid[0])): 
#                 print("inside the normal") 
#                 if j==0:
#                     print("j =0")
#                     arr[i][j][0]=grid[i][j]+arr[i-1][j][1]
#                     arr[i][j][1]=grid[i][j]+arr[i-1][j][1]
#                 if i==0 and j==(len(grid[0])-1):
#                     print("pain point")
#                     print(arr[i][j])
#                     them=max(grid[i][j]+arr[i][j-1][1],grid[i][j]+arr[i][j-1][0])
#                     arr[i][j][0]=them
#                     arr[i][j][1]=them
#                     print("after pain")
#                     print(arr)
#                 if grid[j-1] and not (i == 0 and j == len(grid[0]) - 1) and j != 0:
#                     arr[i][j][0]=grid[i][j]+arr[i][j-1][0]
#                 if grid[j-1] and not (i == 0 and j == len(grid[0]) - 1) and j != 0:
#                     arr[i][j][1]=grid[i][j]+arr[i-1][j][1]

                
#         print("after the whole thing the arr is ")
#         print(arr)

#         return min(
#     arr[len(grid) - 1][len(grid[0]) - 1][0],
#     arr[len(grid) - 1][len(grid[0]) - 1][1]
# )

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
            
        m, n = len(grid), len(grid[0])
        
        # Initialize DP table with the same dimensions as grid
        dp = [[0 for _ in range(n)] for _ in range(m)]
        
        # Fill the first cell
        dp[0][0] = grid[0][0]
        
        # Fill first row
        for j in range(1, n):
            dp[0][j] = dp[0][j-1] + grid[0][j]
        
        # Fill first column
        for i in range(1, m):
            dp[i][0] = dp[i-1][0] + grid[i][0]
        
        # Fill the rest of the DP table
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
        
        return dp[m-1][n-1]

