// // class Solution {
// // public:
// //     int characterReplacement(string s, int k) {
// //         // the approach that we are going to use is that
// //         //we are gonna check penalties for each word if next is not same as it and penalty expired then we move forward storing the num
// //         int t=k;
// //         int longest=0;
// //         char thechar;
// //         int thenum=0;
// //         for (int i=0;i<s.size();i++){
// //             cout<<"checking for the char "<<s[i]<<" at "<<i<<endl;
// // thechar=s[i];
// // for(int j=i;j<s.size();j++){
// //     if(s[j]==thechar){
// //         cout<<"found "<<s[j]<<" at "<<j<<endl;
        
// // thenum++;
// // cout<<"thenum"<<thenum<<endl;
// // continue;
// //     }
// //      if(s[j]!=thechar && t!=0){
// //         t--;
// //         thenum++;
// //         cout<<"currently found "<<s[j]<<" but t ="<<t<<endl;
// //          cout<<"thenum"<<thenum<<endl;
// //     }
// //      if(s[j]!=thechar && t==0){
// //         t=k;
// //         cout<<"cutting because t="<<t<<" and s[j]"<<s[j]<<endl;
// //          cout<<"thenum"<<thenum<<endl;
// //          int m=j+1;
// //          while(s[m]==thechar && k!=0){
// //             if(s[m]==thechar ){
// //                 cout<<"m "<<m<<endl;
            
// //             cout<<s[m]<<"="<<thechar<<endl;
// //             cout<<"incrementing"<<endl;
// //             m++;
// //             thenum++;
// //             }
// //          }
// //         if(longest<thenum){
// //             longest=thenum;
// //         }
// //         cout<<"current longest"<<longest<<endl;
// //         thenum=0;
// //         break;
// //     }
// // }
// // if(longest<thenum){
// //             longest=thenum;
// //         }
// // thenum=0;
// // t=k;
// //         }
// //         return longest;
// //     }
// // };


// // class Solution {
// // public:

// //     int findmaxfreq(unordered_map<char,int> count){
// //         int largest=count['a'];
// //         char thechar;
// //         for (char ch='a';ch!='z';ch++){
// // if(largest<count[ch]){
// //     largest=count[ch];
// //     thechar=ch;
// // }
// //         }
// //         return thechar;
// //     }
// //     int characterReplacement(string s, int k) {

// //         //lets use a new approach
// //         //take a pointer left and a pointer right 
// //         // take a map for the count
// //         //take a has map to store the amount of the each char
        
// //         unordered_map<char,int> count;
// //         for(char  ch='a';ch!='z';ch++){
// // count[ch]=0;
// //         }
// //         int a,b;
// //         a=0;
// //         b=1;
// //         char thechar=s[0];
// //         int longest=0;
// //         int curr;
// //         while(b<s.size()){
// //             thechar=findmaxfreq(count);
// //             cout<<"the maximum is "<<thechar<<endl;
// //             for (int j=a;j<b;j++){
// //          if( count[thechar]-k<=0){
// //             if(s[j]==thechar){
// //                 cout<<"found at "<<j<<" the alphabet"<<thechar<<endl;
// //                 cout<<"the value of s[j]-k s "<<s[thechar]-k<<endl;
// //             }
// //             count[s[j]]++;
// //             curr++;
// //             b++;
// //          }
// //          else if(count[thechar]-k>0){
// //             thechar=findmaxfreq(count);
// //             a++;
// //             count[s[a]]--;
// //             b++;
// //             break;
// //          }
         
// //             }
// //             if(curr>longest){
// //                 longest=curr;
// //             }

// //         }
// // return longest;
// //     }
// // };
// #include <string>
// #include <unordered_map>
// #include <iostream>

// using namespace std;

// class Solution {
// public:

// char findmaxfreq(unordered_map<char,int>& count, int left, int right,string s) {
//     int largest = 0; // Initialize largest count to 0
//     char thechar = 'A'; // Initialize the character with maximum frequency to null character

//     // Iterate over the characters in the interval [left, right]
//     for (int i = left; i <= right; i++) {
//         char ch = s[i]; // Get the current character in the interval
//         largest = max(largest, count[ch]); // Update the largest frequency encountered so far
//     }

//     // Iterate again to find the character with the largest frequency
//     for (int i = left; i <= right; i++) {
//         char ch = s[i]; // Get the current character in the interval
//         if (count[ch] == largest) { // If the current character has the largest frequency
//             thechar = ch; // Update the character with maximum frequency
//             break; // Exit the loop once the character is found
//         }
//     }

//     return thechar;
// }


//     int characterReplacement(string s, int k) {

//         unordered_map<char, int> count;
//         for (char ch = 'A'; ch <= 'Z'; ch++) {
//             count[ch] = 0;
//         }

//         int a = 0, b = 0; // window boundaries
//         int longest = 0, curr = 0;

//         while (b < s.size()) {
//             count[s[b]]++;
//             // cout<<"working on "<<s[b]<<endl;
//     char thechar = findmaxfreq(count,a,b,s);
//     // cout << "Window boundaries (a, b): " << a << ", " << b << endl;
//     // cout << "Current character with max frequency: " << thechar << endl;
//     // cout << "Count of " << thechar << ": " << count[thechar] << endl;

//     if (count[thechar] + k >=( b - a)+1 ) {
//         // cout<<count[thechar]<<endl;
//         // cout << "Entered if" << endl;
//         // cout<<"incrementing"<<s[b]<<" with val "<<count[s[b]]<<endl;
        
//         // cout<<"incremented"<<s[b]<<" with val "<<count[s[b]]<<endl;
//         b++;
//         curr = b - a;
//     } else if(count[thechar] + k <( b - a)+1) {
//         // cout << "Entered else" << endl;
//         count[s[a]]--; // Decrement the count of the character going out of the window
//         a++;
//         b++;
//         curr = b - a;
//     }

//     // cout << "Current substring length: " << curr << endl;
//     longest = max(longest, curr);
//     // cout << "Current longest substring length: " << longest << endl;
//     // cout << "------------------------------------" << endl;
// }

//         return longest;
//     }
// };
 class Solution {
 public:
int characterReplacement(string s, int k) {
    unordered_map<char, int> count;
    int left = 0; // Initialize the left boundary of the window
    int longest = 0; // Initialize the length of the longest substring
    int maxFreq = 0; // Initialize the maximum frequency within the window

    for (int right = 0; right < s.size(); right++) {
        count[s[right]]++; // Increment the count of the current character in the window
        maxFreq = max(maxFreq, count[s[right]]); // Update the maximum frequency within the window

        // If the length of the window minus the maximum frequency is greater than k,
        // we need to shrink the window from the left
        if (right - left + 1 - maxFreq > k) {
            count[s[left]]--; // Decrement the count of the character going out of the window
            left++; // Move the left boundary of the window to the right
        }

        // Update the length of the longest substring
        longest = max(longest, right - left + 1);
    }

    return longest;
}
 };