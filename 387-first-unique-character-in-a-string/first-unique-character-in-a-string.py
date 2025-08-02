from collections import defaultdict

class Solution:
    def firstUniqChar(self, s: str) -> int:
        times=defaultdict(int)
        for i in s:
            times[i]=times[i]+1
        for i in range(len(s)):
            if times[s[i]]==1:
                return i
        return -1



        