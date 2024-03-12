class Solution {
public:
    int maxProfit(vector<int>& prices) {

        // take the minimum and the maximun starting from beginning and then when u see smaller element update small to this and large to this too then move forward checking teh small and large if large found update laege to large anf then find the indexs of the two numbers

        int large=prices[0];
        int small=prices[0];
        int index1;
        int index2;
        vector<int> arr;
        for(int i=0;i<prices.size();i++)
        {
            if(prices[i]<small)
            {
                arr.push_back(large-small);
                small=prices[i];
                index1=i;
                large=prices[i];
            }
            if(prices[i]>large)
            {
                large=prices[i];
                index2=i;
            }
        }
        cout<<small<<endl;
        cout<<large<<endl;

       
        auto maxProfit = std::max_element(arr.begin(), arr.end());

        if (maxProfit != arr.end() && *maxProfit > (large - small)) {
            return *maxProfit;
        } else {
            return large - small;
        }
    }
};