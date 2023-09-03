#include <iostream>
#include <vector>
#include <string>
#include <queue>
#include <unordered_map> // python's dictionary 

using namespace std;

class Solution{
    public:
        string reorganizeString(string s){
            if (s.empty()) return "";

            //Create a max heap using a custom comparator
            // lamdba function in c++  
            // 어떠한 variable에 간단한 function을 assign할때 주로 사용되는 듯. 
            auto cmp = [](pair<int, char> &a, pair<int, char> &b){
                return a.first < b.first;
            };

            //creates `maxHeap` priority queue instance that holds pairs of integers and charcters 
            // the pairs are stored in a vector, and the priority queue uses the `cmp` custom comparator to maintin a max heap structure based on the frequency values in the pairs 
            //decltype : declare type 
            std::priority_queue<pair<int, char>, vector<pair<int, char>>, decltype(cmp)> maxHeap(cmp);

            //Store the letter and frequency as pairs in the max heap 
            unordered_map <char, int> freqCounter;

            for (char c: s){
                freqCounter[c]++;
            }

            for (auto & entry:freqCounter){
                maxHeap.push({entry.second, entry.first});
            }

            std::string res = "";
            auto pre=maxHeap.top();
            maxHeap.pop();
            res += pre.second;

            while (!maxHeap.empty()){
                auto curr = maxHeap.top();
                maxHeap.pop();
                res += curr.second;

                pre.first += 1 ; // Incrementing since max heap was used 

                // If frequency is not exhausted, push back to the heap 
                if (pre.first > 0){
                    maxHeap.push(pre);
                }

                pre = curr;
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