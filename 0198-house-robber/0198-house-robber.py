class Solution:
    def rob(self, nums: List[int]) -> int:
        print(nums)
        if not nums:
            return 0
        if(len(nums)==1):
            return nums[0]
        if(len(nums)==2):
            return max(nums[0],nums[1])
        dp=nums
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2,len(nums)):
            dp[i]=max(dp[i-1],dp[i-2]+nums[i])
            print("current max is ")
            print(dp[i])
        print("dp array is ")
        print(dp)
        print(max(dp))
        return max(dp)

        