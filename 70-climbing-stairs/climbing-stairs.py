class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        
        # Initialize dp array to store number of ways to climb i steps
        dp = [0] * (n + 1)
        dp[1] = 1  # There's only 1 way to climb 1 step
        dp[2] = 2  # There are 2 ways to climb 2 steps (1 + 1 or 2)
        
        # Calculate number of ways for each step starting from 3
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        
        return dp[n]

# Example usage:
solution = Solution()
n = 5
print(solution.climbStairs(n))  # Output: 8
