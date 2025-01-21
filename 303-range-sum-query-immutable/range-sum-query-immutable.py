class NumArray:

    def __init__(self, nums: List[int]):
        self. my_nums=nums

    def sumRange(self, left: int, right: int) -> int:
        the_num=0
        for i in range(left, right+1):
            the_num=self.my_nums[i]+the_num
        return the_num

        
# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)