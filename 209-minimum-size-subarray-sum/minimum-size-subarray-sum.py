class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left=0
        right=0
        counter=1
        arr=[]
        current_total=nums[left]
        if len(nums)==1 and nums[0]>target:
            return 1
        while left!=(len(nums)) and right!=(len(nums)-1) :
            if nums[left]>=target:
                return 1
            right=right+1
            current_total=current_total+nums[right]
            counter=counter+1
            while current_total >= target:
                arr.append(counter)
                current_total -= nums[left]
                counter -= 1
                left += 1
        if arr is not None and len(arr) > 0:
            arr.sort()
            return arr[0]
        else:
            return 0

