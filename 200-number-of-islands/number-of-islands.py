class Solution:
    def __init__(self):
        self.marked = None  # Initialize in numIslands
        self.number = 0
    
    def call_recursive(self, grid, i, j):
        # Check bounds
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
            return
        if grid[i][j] == "0" or self.marked[i][j]:
            return
            
        self.marked[i][j] = True
        self.call_recursive(grid, i+1, j)
        self.call_recursive(grid, i-1, j)
        self.call_recursive(grid, i, j+1)
        self.call_recursive(grid, i, j-1)

    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
            
        self.marked = [[False] * len(grid[0]) for _ in range(len(grid))]
        self.number = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if self.marked[i][j]:
                    continue
                if grid[i][j] == "1":
                    self.call_recursive(grid, i, j)
                    self.number += 1
        
        return self.number