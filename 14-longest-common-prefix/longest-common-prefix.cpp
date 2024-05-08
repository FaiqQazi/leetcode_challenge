// class Solution {
// public:
//     string longestCommonPrefix(vector<string>& strs) {
//         //take the first term and iterate over it to find the longest string
//         if(strs.size()==1 and strs[0]==""){
//             return "";
//         }
//         string returnst="";

//         string mainst;
//         vector<string> vec;
        
//         for (char ch:strs[0]){
//             bool thebool=false;
//             returnst=returnst+ch;
// for(int i=0;i<strs.size();i++){
//     int found=strs[i].find(returnst);
//     if (found != std::string::npos) {
//         cout<<"matched"<<ch<<"in "<<strs[i]<<endl;
        
//     } else {
//         cout<<"not matched"<<ch<<endl;
//         thebool=true;
//         returnst.pop_back();
//         break;
//     }

// }
// if(thebool==true){
//     if(returnst!=""){
// vec.push_back(returnst);
//     }

// for(int j=0;j<vec.size();j++){
//     cout<<"vec "<<vec[j]<<endl;
// }
// returnst="";
// }
//         }
//         vec.push_back(returnst);
//         cout<<"loop ended"<<endl;
//          std::string longest = vec[0];
//          cout<<vec[0]<<endl; // Assume the first string is the longest
// if(vec.size()==1){
//     cout<<"size is 1 return"<<endl;
//     cout<<vec[0];
//     return vec[0];
// }
//     // Iterate through the vector to find the longest string
//     for (const std::string& str : vec) {
//         if (str.length() > longest.length()) {
//             longest = str;
//         }
//     }
//     return longest;
//     }
// };

class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        // Check if the input vector is empty
        if (strs.empty()) {
            return "";
        }
        
        // Iterate over each character in the first string
        for (int i = 0; i < strs[0].size(); ++i) {
            char ch = strs[0][i]; // Get the character at position i
            
            // Iterate over each string in the vector starting from the second string
            for (int j = 1; j < strs.size(); ++j) {
                // Check if the character at position i is out of bounds for the current string or if it doesn't match
                if (i >= strs[j].size() || strs[j][i] != ch) {
                    // If the characters don't match, return the substring from the first string up to position i
                    return strs[0].substr(0, i);
                }
            }
        }
        
        // If all strings have been checked and no mismatches were found, return the first string itself as the common prefix
        return strs[0];
    }
};
