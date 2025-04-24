class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
            
        # Initialize result to handle single character case
        result = s[0]
        
        for i in range(len(s)):
            # Odd length palindromes (centered at i)
            left, right = i, i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                # If current palindrome is longer than our stored result
                if right - left + 1 > len(result):
                    result = s[left:right+1]
                left -= 1
                right += 1
            
            # Even length palindromes (centered between i and i+1)
            left, right = i, i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                # If current palindrome is longer than our stored result
                if right - left + 1 > len(result):
                    result = s[left:right+1]
                left -= 1
                right += 1
                
        return result