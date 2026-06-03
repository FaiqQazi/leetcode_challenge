class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        middle = int(len(arr)/2)
        print(f"middle index is {middle}")
        i=middle
        flag=True
        while flag:
            if arr[i]>arr[i+1] and arr[i]>arr[i-1]:
                flag=False
                return i
            elif arr[i]>arr[i+1] and arr[i-1]>arr[i]:
                i=i-1
            elif arr[i]<arr[i+1] and arr[i-1]<arr[i]:   
                i=i+1
        return i