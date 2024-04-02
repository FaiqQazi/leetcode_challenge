class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
 unordered_map<int,int> map;
     vector<int> v;

 for(int i=0;i<nums.size();i++)
 {
map.insert(make_pair(nums[i], i));
 }
 for(int i=0;i<nums.size();i++)
 {
    int index=target-nums[i];
    auto it=map.find(index);
    if (it != map.end() && it->second!=i) {
    std::cout << "Found key  " <<it->first<<"with index "<< it->second << std::endl;
    v.push_back(i);
    cout<<"pushed "<<nums[i]<<"with index "<<i<<endl;
    v.push_back(it->second);
    break;
} else {
    std::cout << "Key 2 not found" << std::endl;
}
 }
     return v;

    }
};






// int* hash = new int[2*pow(10,9)]; // Dynamically allocate memory for the array
//         memset(hash, 0, 2*pow(10,9)*sizeof(int));        for(int i=0;i<nums.size();i++)
//         {
//             hash[nums[i]+pow(10,9)]=nums[i];
//         }

//         for(int i=0;i<nums.size();i++)
//         {
//             if(hash[target-(nums[i]+pow(10,9)]!=0)
//             {
//                 vector<int> vv;
//                 vv.push_back(nums[i]);

//             }
//         }
//         //now that we know the first element that matches nad the target we can get the second element in o(n) with search 
//         for(int i=0;i<nums.size();i++)
//         {
//             if(nums[i]==target-vv[0])
//             {
//                 vv.push_back(nums[i]);
//             }
//         }
//         return vv;
//     }