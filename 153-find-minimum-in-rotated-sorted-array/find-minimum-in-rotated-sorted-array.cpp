#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int findMin(vector<int>& nums) {

        
        int left = 0;
        int right = nums.size() - 1;
// if(nums[right]-nums[left]==nums.size()-1)
// {
//     if(nums[0]<nums[nums.size()-1])
//     {
//         return nums[0];
//     }
//     else
//     {
//         return nums[nums.size()-1];
//     }
// }
        while (left < right) {
            int middle = left + (right - left) / 2;

            // Check if the first element is larger than the last
            if (nums[middle] > nums[right]) {
                // Move the last element to the middle
                left = middle+1;
            } else {
                // Move the first element to the middle + 1
                right=middle;
            }
        }

        // The loop exits when left == right (crossing point)
        return nums[left];
    }
};


