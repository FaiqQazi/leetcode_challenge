class Solution:
    def find_max(self,arr):

        max_num = arr[0]  # Start by assuming the first element is the maximum
        for num in arr:
            if num > max_num:
                max_num = num  # Update if a larger number is found
        return max_num


    def lengthOfLIS(self, nums: List[int]) -> int:
        arr=[1]*len(nums)
        print(arr)
        for i in reversed(range(len(nums))):
            if i + 1 >= len(nums):
                continue  # Skip if t
            greater_indexes = [index for index, num in enumerate(nums[i:], start=i) if num > nums[i]]
            arr_new = [arr[index] for index in greater_indexes]
            if arr_new:  # This checks if the list is not empty
                arr[i] = arr[i] + max(arr_new)
            else:
                arr[i] = arr[i]  # Or just leave it unchanged, or handle it as you like
             
            # for j in range(i,len(nums)):
            #         if nums[j]>nums[i]:
            #             arr[i]=arr[j]+arr[i]
            #             break
        print("this is the main dp array")
        print(arr)
        z=self.find_max(arr)
        print(z)
        return z



        