# class Solution:
#     def maxDistance(self, arrays: List[List[int]]) -> int:
#         m=True
#         while m:
#             print(arrays)
#             arr_min=[]
#             arr_max=[]
#             for m in arrays:
#                 arr_min.append(m[0])
#             for m in arrays:
#                 arr_max.append(m[-1])
#             small=min(arr_min)
#             print("smallest is ")
#             print(small)
#             big=max(arr_max)
#             print("bigger  is ")               
#             print(big)
#             result=big-small
#         return result


class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        min_val=arrays[0][0]
        min_index=0
        max_val=arrays[0][-1]
        max_index=0
        result=0
        for i in range(1,len(arrays)):
            curr_min = arrays[i][0]
            curr_max = arrays[i][-1]

            # If min and max from different arrays, calculate
            result = max(result, abs(curr_max - min_val), abs(max_val - curr_min))
            if curr_min<min_val:
                min_val=curr_min
                min_index=i
            if curr_max>max_val:
                max_val=curr_max
                max_index=i
        return result



        