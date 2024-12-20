class Solution {
public:
    int lengthOfLongestSubstring(string s) {

        unordered_set<char> charset(s.begin(),s.end());
        unordered_map<char,int> charmap;
        string returnst="";
        vector<string> vec;
        int t=0;
        for(char ch:charset){
            charmap[ch]=0;
        }
        for (int i=0;i<s.size();i++){
            // cout<<"i value"<<i<<endl;
            // cout<<"working on "<<s[i]<<endl;
if(charmap[s[i]]==0){
returnst+=s[i];
charmap[s[i]]=1;
continue;

}
else{
    // cout<<"pushed"<<returnst<<endl;
vec.push_back(returnst);
returnst="";
t++;
i=t;
for (auto& pair : charmap) {
        pair.second = 0; // Reset all character occurrences to 0
    }
    i--;
}
        }
        vec.push_back(returnst);
        // cout<<"last "<<returnst<<endl;
        string longest = "";
        for (const string& str : vec) {
    if (str.length() > longest.length()) {
        longest = str;
    }
}
return longest.length();
    }
};
// #include <string>
// #include <vector>
// #include <algorithm> // for std::find
// #include <cmath>     // for std::max

// using namespace std;

// class Solution {
// public:
//     int lengthOfLongestSubstring(string s) {
//         int n = s.length();
//         vector<char> window;
//         int maxlength = 0;
//         for (int i = 0; i < n; i++) {
//             auto it = find(window.begin(), window.end(), s[i]);
//             if (it != window.end()) {
//                 window.erase(window.begin(), it + 1);
//             }
//             window.push_back(s[i]);
//             maxlength = max(maxlength, static_cast<int>(window.size()));
//         }
//         return maxlength;
//     }
// };
