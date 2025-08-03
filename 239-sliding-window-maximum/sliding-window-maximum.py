from typing import List
from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        d=deque()
        arr=[]
        for i in range(len(nums)):
            if d and d[0]<((i-k)+1):
                c=d.popleft()
                print(c)
            while d and nums[i]>nums[d[-1]]:
                n=d.pop()
                print(n)
            d.append(i)
            if d and i+1>=k:
                arr.append(nums[d[0]])

        return arr

