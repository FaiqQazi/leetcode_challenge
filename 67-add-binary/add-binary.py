class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a=int(a, 2)
        print(a)
        b=int(b,2)
        print(b)
        num=a+b
        bin_num=bin(num)
        print(bin_num)
        return bin_num[2:]