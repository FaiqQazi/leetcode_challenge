class Solution:

    def longestPalindrome(self, s: str) -> str:
        if(len(s)==1):
            return s
        left=0
        right=len(s)-1

        arr=[]

        for i in range (0, len(s)-1):
            m=True
            curr_str=s[i]
            left=i-1
            right=i+1
            while left >= 0 and right < len(s) and s[left] == s[right]:

                curr_str=s[right]+curr_str+s[left]
                left=left-1
                right=right+1
            arr.append(curr_str)
            left = i
            right = i + 1
            curr_str = ""
            
            while left >= 0 and right < len(s) and s[left] == s[right]:
                curr_str = s[left] + curr_str + s[right]
                left -= 1
                right += 1
            
            if curr_str:  # Only add if we found an even-length palindrome
                arr.append(curr_str)


        sorted_arr=sorted(arr,key=len)
        print("the sorted arr is ")
        print(sorted_arr)
        print("the final element is ")
        return  max(arr, key=len) 

                



        