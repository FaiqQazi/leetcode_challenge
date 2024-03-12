class Solution {
public:
    bool isPalindrome(int x) {
        string str=to_string(x);
        int j=str.length()-1;
        bool b=true;
        for(int i=0;i<str.length()/2;i++)
        {
            if(str[i]!=str[j])
            {
                return false;
            }
            j--;
        }
        return true;
    }
};