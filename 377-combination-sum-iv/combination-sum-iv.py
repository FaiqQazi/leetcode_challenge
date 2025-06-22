# class Solution:
#     def combinationSum4(self, nums: List[int], target: int) -> int:
#         marked = []
#         check_list = []
#         print(f"Initial nums: {nums}, target: {target}")
        
#         for n in nums:
#             if n < target:
#                 check_list.append([n])
#                 print(f"Starting new check_list with: {[n]}")
#             elif n == target:
#                 marked.append([n])
#                 print(f"Found exact match with: {[n]}")

#         while check_list:
#             print(f"\nCurrent check_list: {check_list}")
#             current_level = check_list[:]
#             check_list = []

#             for arr in current_level:
#                 print(f"Checking array: {arr}")
#                 current_sum = sum(arr)

#                 for nn in nums:
#                     new_sum = current_sum + nn
#                     new_arr = arr + [nn]
#                     print(f"  Trying to add {nn}: new arr = {new_arr}, sum = {new_sum}")

#                     if new_sum < target:
#                         check_list.append(new_arr)
#                         print(f"    Under target, added to check_list")
#                     elif new_sum == target:
#                         marked.append(new_arr)
#                         print(f"    Match found! Added to marked: {new_arr}")
#                     else:
#                         print(f"    Over target, skipped")

#         print(f"\nFinal marked combinations: {marked}")
#         return len(marked)


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp=[0]*(target+1)
        dp[0]=1
        for target in range(1,target+1):
            for num in nums:
                if target-num>=0:
                    dp[target]=dp[target]+dp[target-num]
        return dp[target]