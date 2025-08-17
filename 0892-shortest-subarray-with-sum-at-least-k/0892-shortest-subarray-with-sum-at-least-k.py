from collections import deque
class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        arr=[0]
        for i in range(len(nums)):
            # print(f"arr [i] is {arr[i]}")
            # print(f"nums[i] is {nums[i]}")
            arr.append(arr[i]+nums[i])
            # print(f"appended {arr[i]+nums[i]}")
        # print("after doing the prefix sum the arr is ")
        # print(arr)
        d=deque([0]) #to store the indexes
        s=[]# to store the values of the indexes
        minl=float("inf")
        for i in range(len(arr)):
            # print(f"entered into the loop for {i} and the arr value is {arr[i]}")
            while d and arr[i]-arr[d[0]]>=k:
                # print(f"arr[i]-arr[d[0]] is {arr[i]-arr[d[0]]} which is greator then {k} so pop left")
                minl=min(minl,i-d.popleft())
                # print(f"d is {d}")
            while d and arr[i]<arr[d[-1]]:
                # print(f"arr[i]<arr[d[-1]] is {arr[i]<arr[d[-1]]} popping right")
                d.pop()
                # print(f"d is {d}")
            d.append(i)
        # print(f"the minl is {minl}")
        if minl!=float("inf"):
            return minl
        else:
            return -1



        
        
        