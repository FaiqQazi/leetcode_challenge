class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        // sort each of the strings
        vector<string> newarr;
        for(int i=0;i<strs.size();i++){
            newarr.push_back(strs[i]);
        }
        for(int i=0;i<strs.size();i++){
            cout<<newarr[i]<<endl;
            sort(newarr[i].begin(),newarr[i].end());
            cout<<newarr[i]<<endl;
        }
        unordered_map <string,vector<string>> themap;
        vector<vector<string>> thest;
        for(int i=0;i<newarr.size();i++){
        themap[newarr[i]].push_back(strs[i]);
        }
        for (auto& pair : themap) {
        // Iterate through the vector of strings for each key
        for (const string& str : pair.second) {
            // Append each string to the vector<vector<string>>
            
            cout<<str<<" ";
        }
        thest.push_back(pair.second);
        cout<<endl;
    }
    return thest;
    }
};