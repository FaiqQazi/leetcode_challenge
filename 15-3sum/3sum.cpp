// class Solution {
// public:
//     vector<vector<int>> threeSum(vector<int>& nums) {
//         //sort it 
//         vector<vector<int >> v;
// sort(nums.begin(), nums.end());
//         for(int i=1;i<nums.size();i++)
//         {
//            int j=i-1;
//             int k=i+1;
//             while(1)
//             {
            
//                 if(nums[i]+nums[j]+nums[k]==0)
//                     {
//                      vector<int > vv;
//                         vv.push_back(nums[i]);
//                         vv.push_back(nums[j]);

//                         vv.push_back(nums[k]);

//                         v.push_back(vv);
//                     }
//             if(nums[i]+nums[j]+nums[k]<0)
//             {
//                 k++;
//                 if(k==nums.size()-1)
//                 {
//                     break;
//                 }
//             }
//             else if(nums[i]+nums[j]+nums[k]>0)
//             {
//                 j--;
//                 if(j==0)
//                 {
//                     break;
//                 }
//             }
//             }
            
           
//         }
// return v;
//     }
// };
// int main() {
//     // Test cases
//     vector<int> nums1 = {-1, 0, 1, 2, -1, -4};
//     vector<int> nums2 = {0, 1, 1};
//     vector<int> nums3 = {0, 0, 0};

//     Solution sol;

//     cout << "Test Case 1:" << endl;
//     vector<vector<int>> result1 = sol.threeSum(nums1);
//     for(auto triplet : result1) {
//         for(int num : triplet) {
//             cout << num << " ";
//         }
//         cout << endl;
//     }

//     cout << "Test Case 2:" << endl;
//     vector<vector<int>> result2 = sol.threeSum(nums2);
//     for(auto triplet : result2) {
//         for(int num : triplet) {
//             cout << num << " ";
//         }
//         cout << endl;
//     }

//     cout << "Test Case 3:" << endl;
//     vector<vector<int>> result3 = sol.threeSum(nums3);
//     for(auto triplet : result3) {
//         for(int num : triplet) {
//             cout << num << " ";
//         }
//         cout << endl;
//     }

//     return 0;
// }


//         //     int j=i-1;
        
//         //     if(nums[i]+nums[j]<nums[i])
//         //     {
//         //         for(int k=i+1;k<nums.size();k++)
//         //         {
//         //             if(nums[i]+nums[j]+nums[k]==0)
//         //             {
//         //                 int vector<int > vv;
//         //                 vv.push_back(nums[i]);
//         //                 vv.push_back(nums[j]);

//         //                 vv.push_back(nums[k]);

//         //                 v.push_back(vv);

//         //             }
//         //         }
//         //     }
//         //     else if()
//         //     {

//         //     }
            
//         // }


class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        // Sort the array
        sort(nums.begin(), nums.end());
        
        // Vector to store the result
        vector<vector<int>> v;

        // Iterate through the array
        for(int i = 0; i < nums.size() - 2; i++) {
            // Skip duplicates
            if (i > 0 && nums[i] == nums[i - 1]) continue;

            int j = i + 1;
            int k = nums.size() - 1;

            // Two-pointer approach
            while(j < k) {
                int sum = nums[i] + nums[j] + nums[k];
                if(sum == 0) {
                    v.push_back({nums[i], nums[j], nums[k]});
                    
                    // Skip duplicates
                    while(j < k && nums[j] == nums[j + 1]) j++;
                    while(j < k && nums[k] == nums[k - 1]) k--;
                    
                    j++;
                    k--;
                } else if(sum < 0) {
                    j++;
                } else {
                    k--;
                }
            }
        }
        return v;
    }
};
