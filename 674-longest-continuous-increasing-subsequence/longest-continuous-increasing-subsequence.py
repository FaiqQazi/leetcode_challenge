class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if not nums:
            print("Input list is empty. Returning 0.")
            return 0
        
        longest = 1
        arr = []
        print(f"Starting traversal of nums: {nums}")
        
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                longest += 1
                print(f"  Increasing longest to {longest}")
            else:
                arr.append(longest)
                longest = 1
                print("  Reset longest to 1")
        
        # After loop ends, add the last counted sequence length
        if not arr:
            arr.append(longest)
            print(f"Array arr was empty, appended longest = {longest}")
        else:
            arr.append(longest)
            print(f"Appending last longest = {longest} to arr: {arr}")
        
        send = max(arr)
        print(f"Longest continuous increasing subsequence lengths: {arr}")
        print(f"Maximum length found: {send}")
        
        return send
