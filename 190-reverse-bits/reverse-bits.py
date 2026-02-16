class Solution:
    def reverseBits(self, n: int) -> int:
        bin_num=format(n,'032b')
        # print(bin_num)
        bin_str=str(bin_num)
        # print(bin_str)
        # print(type(bin_str))
        new_str=""
        for char in reversed(bin_str):
            new_str=new_str+char
        # print(f"the new str is reversed is {new_str}")
        decimal_num=int(new_str,2)
        # print(decimal_num)
        return decimal_num

        