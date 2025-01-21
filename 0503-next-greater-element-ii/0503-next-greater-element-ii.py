# class Solution:
#     def nextGreaterElements(self, nums: List[int]) -> List[int]:
#         # Remove 'int' declarations as Python is dynamically typed
#         arr = []
#         final_arr = []
        
#         # Fix nums.length to len(nums)
#         left = 0
#         right = 1
#         arr = nums + nums  # This creates a concatenated list
#         while(len(final_arr)<=len(nums)-1):
#             if(len(final_arr)==len(nums)):
#                 return final_arr
#             if arr[left]==max(nums):
#                 final_arr.append(-1)
#                 left=left+1
#                 right=left+1
#                 continue
#             if arr[left] >= arr[right]:
#                 right += 1
#             elif arr[left]<arr[right]:
#                 final_arr.append(arr[right])
#                 left += 1
#                 right = left + 1
                
#         return final_arr

#         #Time Limit Exceeded 217 / 223 testcases passed
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [-1] * n  # Initialize all elements in the result array to -1
        stack = []  # Stack to store indices of elements in the array
        
        # Traverse the array twice (simulate circular array)
        for i in range(2 * n):  # Loop over the array twice
            num = nums[i % n]  # This simulates the circular traversal
            # While the stack is not empty and the current element is greater than the element at the top of the stack
            while stack and nums[stack[-1]] < num:
                index = stack.pop()  # Pop the index of the element that has a smaller value
                result[index] = num  # Update the result array with the next greater element
            if i < n:  # Only push indices during the first pass
                stack.append(i)
        
        return result
