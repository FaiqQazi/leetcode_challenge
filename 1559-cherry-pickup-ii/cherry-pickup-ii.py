from collections import deque
from typing import List

class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        def valid(cell):
            return 0 <= cell[0] < rows and 0 <= cell[1] < cols
        
        rows = len(grid)
        cols = len(grid[0]) if rows > 0 else 0

        # best cumulative score reaching each (cell1, cell2) pair
        best_at = {}
        start_pair = ((0,0), (0, cols-1))
        if cols > 1:
            best_at[start_pair] = grid[0][0] + grid[0][cols-1]
        else:
            best_at[start_pair] = grid[0][0]

        q = deque()
        q.append(start_pair)
        visited = set()
        visited.add(start_pair)

        while q:
            cell1, cell2 = q.popleft()
            for d1 in [-1, 0, 1]:
                for d2 in [-1, 0, 1]:
                    new_cell1 = (cell1[0]+1, cell1[1]+d1)
                    new_cell2 = (cell2[0]+1, cell2[1]+d2)
                    if valid(new_cell1) and valid(new_cell2):
                        if new_cell1 == new_cell2:
                            score = grid[new_cell1[0]][new_cell1[1]]
                        else:
                            score = grid[new_cell1[0]][new_cell1[1]] + grid[new_cell2[0]][new_cell2[1]]
                        
                        new_pair = (new_cell1, new_cell2)
                        cumulative = best_at[(cell1, cell2)] + score
                        
                        if new_pair not in best_at:
                            best_at[new_pair] = cumulative
                        else:
                            best_at[new_pair] = max(best_at[new_pair], cumulative)
                        
                        if new_pair not in visited:
                            visited.add(new_pair)
                            q.append(new_pair)

        return max(v for (c1, c2), v in best_at.items() if c1[0] == rows-1)