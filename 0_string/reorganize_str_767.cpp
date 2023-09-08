/*

input: string s
goal: rearrange the characters of s so that any two adjacent characters are not the same 
output: rearranged string 

ex) 
s = "aab" 
output = "aba" 

s = "aaab" 
output = "" 

*/
#include <iostream>
#include <unordered_map> 
#include <queue> // priority queue , push, pop & top, empty, size 
#include <utility> //pair 
#include <string> // string 
using namespace std;

class Solution {
public:
    string reorganizeString(string s) {
        if (s.empty()) return "";

        // Counter 
        unordered_map<char, int> cnt;
        
        for (char c : s){
            cnt[c]++;
        }

        // max-heap comparator  
        //어떠한 variable에 간단한 function을 assign할 때 주로 사용됨 
        auto cmp = [](pair<char, int> &a, pair<char, int> & b){
            return a.second < b.second; // dictionary의 key를 비교 
        }; // lambda fucntion 뒤에는 ; 를 써야한다!!!

        //decltype : declare type 
        std:priority_queue<pair<char, int>, vector<pair<char, int>>, decltype(cmp)> maxHeap(cmp);
        
        for (auto & entry: cnt){
            maxHeap.push({entry.first, entry.second}); // pair는 make_pair(1, 'a') 아니면 {1, 'a'}로 initialization할 수 있다. 
        }

        // make result 
        string res("");
        pair<char, int> pre = maxHeap.top();
        maxHeap.pop();
        res += pre.first;
       

        while (!maxHeap.empty()){
            pair<char, int> cur = maxHeap.top();
            maxHeap.pop();
            res += cur.first;

            pre.second -= 1;
            // If frequency is not exhausted, push back to the heap 
            if (pre.second > 0){
                maxHeap.push(pre);
            }

            pre = cur; 
        }

        // (condition) ? value_a : value_b; 
        // if the condition is true, return value_a otherwise return value_b
        return (res.length() != s.length()) ? "" : res;



    }
};


int main() {
    Solution sol;
    std::string input = "aab";
    std::string result = sol.reorganizeString(input);
    std::cout << result << std::endl;
    return 0;
}