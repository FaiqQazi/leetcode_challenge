class Solution:

    
    def binary_search_with_range(self,arr, target):
        left, right = 0, len(arr) - 1
        lower_bound, upper_bound = None, None
        while left <= right:
            mid = (left + right) // 2   
            print(f"the arr[mid] is {arr[mid]} and the target is {target} thats it")
            if arr[mid] == target:
                print(f"returning {arr[mid]}")
                return arr[mid], None, None
            elif arr[mid] < target:
                lower_bound = arr[mid]
                left = mid + 1
            else:
                upper_bound = arr[mid]
                right = mid - 1            
        return None, lower_bound, upper_bound

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        arr_col=[]
        for r in matrix:
            arr_col.append(r[0])
        print(f"arr_col is {arr_col}")
        target_temp , lower , upper=self.binary_search_with_range(arr_col,target)
        if target_temp!=None:
            return True
        print(lower)
        print(upper)
        print(f"the target temp in this case is {target_temp}")
        print(f"the lower in this case is {lower}")
        print(f"the upper in this case is {upper}")
        if not lower :
            index=arr_col.index(upper)
        else:
            index=arr_col.index(lower)
        print(index)
        print(f"the matrix index is {matrix[index]}")
        final_target , final_lower , final_upper=self.binary_search_with_range(matrix[index],target)
        if final_target:
            return True
        else:
            return False
