from typing import List
import heapq
from math import inf
class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        # # arr=[]
        # # vals_arr=[]
        # max_val = float('-inf')
        # for i in range (len(points)):
        #     # print(f"i is {i} and points[i] is {points[i]}")
        #     for j in range (i+1,len(points)):
        #         # print(f"j is {j} and points[j] is {points[j]}")
        #         cond=abs(points[i][0]-points[j][0])
        #         if cond<=k:
        #             # arr.append([i,j])
        #             # print(f"condition holds abs(points[i][0]-points[j][0]) is {abs(points[i][0]-points[j][0])}")
        #             val = points[i][1] + points[j][1] + (points[j][0] - points[i][0])
        #             max_val = max(max_val, val)
        #         else:
        #             # print(f"condition not holds abs(points[i][0]-points[j][0]) is {abs(points[i][0]-points[j][0])} breaking")
        #             break
        # # for i in range(len(arr)):
        # #     val=points[arr[i][0]][1]+points[arr[i][1]][1]+abs(points[arr[i][0]][0]-points[arr[i][1]][0])
        # #     vals_arr.append(val)
        # # return max(vals_arr)
        # return max_val

        max_val=float("-inf")
        min_heap=[]
        for x,y in points:
            while min_heap and x-min_heap[0][1]>k:
                heapq.heappop(min_heap)
            if min_heap:
                max_val=max(max_val,x+y-min_heap[0][0])
            heapq.heappush(min_heap, (x -y,x))
        return max_val



                
        