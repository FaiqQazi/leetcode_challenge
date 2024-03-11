

// class Solution {
// public:
//     vector<int> productExceptSelf(vector<int>& nums) {
//         //so what we will do is that iterate througbh the array from the front and from the back too ateach step we will the 
//         //cummultative multiplication as in if address is 2 then in address two the multiplication of all before it will be stored 
//        if(nums.size()==2)
//        {
//         cout<<"size is 2"<<endl;
//         int temp;
//         temp=nums[0];
//         nums[0]=nums[1];
//         nums[1]=temp;

//         return nums;
//        }
//        vector<int>left;
//        vector<int>right;

//        for(int i=0;i<nums.size();i++)
//        {
//            left.push_back(nums[i]);
//        }
//         for(int i=0;i<nums.size();i++)
//        {
//         cout<<left[i]<<endl;
//        }
       
//        for(int i=0;i<nums.size();i++)
//        {
//            right.push_back(nums[i]);
//        }
//         for(int i=0;i<nums.size();i++)
//        {
// cout<<right[i]<<endl;    
//    }
//         for(int i=1;i<nums.size();i++)
//         {
//             cout<<"multiplying"<<left[i]<<"with "<<left[i-1]<<endl;
//            left[i]=left[i]*left[i-1];
//         }
//          for(int i=0;i<nums.size();i++)
//        {
// cout<<left[i]<<endl;       }
//         for(int i=nums.size()-2;i>=0;i--)
//         {
//          cout<<"multiplying"<<right[i]<<"with "<<right[i+1]<<endl;

//             right[i]=right[i]*right[i+1];
//         }
//         for(int i=0;i<nums.size();i++)
//        {
// cout<<right[i]<<endl;    
//    }
//         vector<int>answer;
//         for(int i=0;i<nums.size();i++)
//         {
            
//             int ans=left[i]*right[i];
//             answer.push_back(ans);
//         }
//         cout<<"printing the array before division"<<endl;
//          for(int i=0;i<nums.size();i++)
//         {
//             cout<<answer[i]<<endl;
//         }
//          for(int i=0;i<nums.size();i++)
//         {
//             if(nums[i]==0)
//             {
//                 if(i==0)
//                 {
//                     answer[i]=right[i+1];
//                     continue;
//                 }
//                 if(i==nums.size()-1)
//                 {
//                     answer[i]=left[i-1];
//                     continue;
//                 }
//                 answer[i]=left[i-1]*right[i+1];
//             }
//         }
//         for(int i=0;i<nums.size();i++)
//         {
//             if(nums[i]==0)
//             {
// continue;
//             }
//             answer[i]=answer[i]/(nums[i]*nums[i]);
//         }
//                 for(int i=0;i<nums.size();i++)
//         {
//             cout<<answer[i]<<endl;
//         }
//         return answer;
        
        
//     }
// };

class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        // Initialize left and right arrays to store cumulative products
        vector<int> left(nums.size(), 1);
        vector<int> right(nums.size(), 1);
        vector<int> answer(nums.size(), 1);

        // Calculate cumulative products from the left side
        for(int i = 1; i < nums.size(); i++) {
            left[i] = left[i - 1] * nums[i - 1];
        }

        // Calculate cumulative products from the right side
        for(int i = nums.size() - 2; i >= 0; i--) {
            right[i] = right[i + 1] * nums[i + 1];
        }

        // Calculate the product except self for each element
        for(int i = 0; i < nums.size(); i++) {
            answer[i] = left[i] * right[i];
        }

        return answer;
    }
};
