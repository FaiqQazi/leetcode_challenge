class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        new_nums=sorted(nums)
        # print(nums)
        # print(new_nums)
        num_set=sorted(set(new_nums))
        # print(num_set)
        count=0
        max_count=0
        for i in range(len(num_set)-1):
            # print(f"current number is {num_set[i]} and the next number is {num_set[i+1]}")
            if num_set[i]+1==num_set[i+1]:
                count=count+1
                # print(f"count changed to {count}")
                max_count=max(max_count,count)
            else:
                max_count=max(max_count,count)
                # print(f"max count is {max_count}")
                count=0
        return max_count+1
        