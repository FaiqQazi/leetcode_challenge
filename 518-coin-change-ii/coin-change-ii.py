# class Solution:
#     def change(self, amount: int, coins: List[int]) -> int:
#         total=0
#         dp={}
#         def backtrack(total):
#             if total==amount:
#                 print(total,"and",amount)
#                 return 1
#             if total>amount:
#                 print("not valid")
#                 return 0
#             if total in dp:
#                 return dp[total]
            
#             if total<amount:
#                 print("currently total is ",total)
#                 n=0
#                 for num in coins:
#                     print("entered again")
#                     print("going for",num)
#                     n+=backtrack(total+num)
#                 dp[total]=n
#                 return n
#         p=backtrack(0)
#         return p

           

from typing import List

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = {}
        
        def backtrack(total, index):
            if total == amount:
                return 1
            if total > amount:
                return 0
            if (total, index) in dp:
                return dp[(total, index)]
            
            count = 0
            for i in range(index, len(coins)):
                count += backtrack(total + coins[i], i)
            
            dp[(total, index)] = count
            return count
        
        return backtrack(0, 0)
