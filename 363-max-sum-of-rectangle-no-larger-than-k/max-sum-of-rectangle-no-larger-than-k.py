import bisect
class Solution:
    # def rect_sum(self, prefix, top, bottom, left, right):
    #     r1, c1 = top+1, left+1
    #     r2, c2 = bottom+1, right+1
    #     return (
    #         prefix[r2][c2]
    #         - prefix[r1-1][c2]
    #         - prefix[r2][c1-1]
    #         + prefix[r1-1][c1-1]
    #     )
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
    #     i=0
    #     arr=set()
    #     m=len(matrix)
    #     print(m)
    #     n=len(matrix[0])
    #     print(n)
    #     prefix = [[0] * (n+1) for _ in range(m+1)]

    #     for r in range(1, m+1):
    #         for c in range(1, n+1):
    #             prefix[r][c] = (
    #                 matrix[r-1][c-1]
    #                 + prefix[r-1][c]
    #                 + prefix[r][c-1]
    #                 - prefix[r-1][c-1]
    #             )
    #     best = float('-inf')
    #     for top in range(m):
    #         for bottom in range(top,m):
    #             for left in range(n):
    #                 for right in range(left,n):
    #                     s = self.rect_sum(prefix,top, bottom, left, right)
    #                     if s <= k:
    #                         best = max(best, s)
    #                     i=i+1

    #     return best

        
        rows=len(matrix)
        columns=len(matrix[0])
        best = float("-inf")
        for top in range(0,rows):
            temp = [0] * columns
            for bottom in range(top,rows):
                for cols in range(0,columns):
                    temp[cols] += matrix[bottom][cols]
                prefix=0
                ts=[0]
                max_sum = float("-inf")
                for x in temp:
                    prefix=prefix+x
                    idx=bisect.bisect_left(ts,prefix-k)
                    if idx<len(ts):
                        max_sum = max(max_sum, prefix - ts[idx])
                    bisect.insort(ts, prefix)
                best = max(best, max_sum)
        return best
                





                    


         

        