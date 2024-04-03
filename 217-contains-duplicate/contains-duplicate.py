# from typing import List

# class Solution:
#     @staticmethod
#     def maxx(nums: List[int]) -> int:
#         return max(nums)

#     def containsDuplicate(self, nums: List[int]) -> bool:
#         m = max(nums)
#         listt = [0] * (m + 1)  # Initialize listt before the loop
#         for index in nums:
#             listt[index] += 1
#         for index in listt:
#             if index > 1:
#                 return True
#         return False


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        s=set()
        for index in nums:
            if(index in s):
                return True
            else:
                s.add(index)
        return False