# class Solution:
#     def wordBreak(self, s: str, worddict: List[str]) -> bool:
#         thestr=""
#         for letter in s:
#             thestr=thestr+letter
#             print("current string ",thestr)
#             for word in worddict:
#                 if(thestr == word):
#                     print("matched the word", word, "with the thestr", thestr)
#                     thestr=""
#                     break
#         if(len(thestr)==0):
#             return True
#         else:
#             return False


class Solution:
    def wordBreak(self, s: str, worddict: List[str]) -> bool:
        n=len(s)

        dp=[False]*(n+1)
        dp[0]=True
        for i in range(1,n+1):
            for j in range(i):
                if dp[j] and s[j:i] in worddict:
                    dp[i] = True
                    break
    
        return dp[n]