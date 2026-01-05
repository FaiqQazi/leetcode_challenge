class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxi=0
        l=0
        r=len(height)-1
        print(f"l is {l} and r is {r}")
        while l!=r:
            print(f"water is {r-l} multiply {min(height[l],height[r])}")
            water=((r-l))*min(height[l],height[r])
            print(water)
            maxi=max(maxi,water)
            if height[l]>=height[r]:
                r=r-1
            else:
                l=l+1
        return maxi

        