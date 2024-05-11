class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        // for (int i=0;i<nums.size()-1;i++){
        //     if(nums[i]==nums[i+1]){
        //         cout<<"printing nums[i]"<<nums[i]<<" at "<<i<<endl;
        //         nums.erase(nums.begin()+i);
        //     }
        // }
        // return nums.size();

        // make a stack
        stack<int> st;
        while(nums.empty()==false){
            int num=nums.back();
            nums.pop_back();
            st.push(num);
            cout<<"pushing "<<num
<<"in to the stack"<<endl;
        }
        
        int j=0;
        cout<<"is the vector empty "<<nums.empty()<<endl;
        while(st.empty()==false){
            int num=st.top();
            cout<<"working on "<<num<<endl;
            if(j==0){
            nums.push_back(num);
            j++;
            st.pop();
            }
            else if(j!=0 && num==nums[j-1]){
                cout<<"num == nums[j]"<<num<<nums[j]<<endl;
                j++;
                st.pop();
            }
            else if(j!=0 && num!=nums[j-1]){
                j++;
                nums.push_back(num);
                cout<<"simply pushing "<<num<<endl;
                st.pop();
            }
           

        }
        return nums.size();
    }
};