class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left = 0
        right = num
        
        while left <= right:
            middle = left + (right - left) // 2
            square = middle * middle
            
            if square == num:
                return True
            elif square < num:
                left = middle + 1
            else:
                right = middle - 1
                
        return False

def main():
    # Test cases
    solution = Solution()
    print(solution.isPerfectSquare(16))  # Output: True
    print(solution.isPerfectSquare(14))  # Output: False

if __name__ == "__main__":
    main()
