class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        bin_num=bin(n)
        print(bin_num)
        bin_num=bin_num[2:]
        print(bin_num)
        for i in range(len(bin_num)-1):
            if bin_num[i]==bin_num[i+1]:
                return False
        return True

        