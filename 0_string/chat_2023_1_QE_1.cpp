#include <iostream>
#include <unordered_map> // python 의 dic과 동일. find(key), count(key) insert(key, value) erase(key) clear 
#include <unordered_set> // set used to store the adjacency list of a certain char 
#include <vector>
using namespace std;



string foo(const string& s) {
//'abcd' => 'acdb' (x) 
    if (s.size() <= 4){
        return "";
    }
    string result ;
    for (int i = 0; i < s.size(); i+=2){
        result += s[i];
    }
    for (int i = 1; i < s.size(); i+=2){
        result += s[i];
    }
    return result;
} 

// ans를 global variable을 지정해주어 func와 bar 모두에서 해당 variable을 사용할 수 있도록 해준다. 
string ans;

void func(unordered_map<char, int>& cnt, int used, vector<char>& buf, unordered_map<char, unordered_set<char>>& adj) {
    if (used >= cnt.size()) {
        ans = string(buf.begin(), buf.end());
        return;
    } else {
        for (auto& pair : cnt) {
            char i = pair.first;
            if (pair.second <= 0) {
                continue;
            } else {
                if (buf.empty() || adj[buf.back()].find(i) == adj[buf.back()].end()) {
                    unordered_map<char, int> cnt_new = cnt;
                    cnt_new[i] = cnt_new[i] - 1;
                    buf.push_back(i);
                    func(cnt_new, used + 1, buf, adj);
                    buf.pop_back();
                }
            }
        }
    }
}

string bar(const string& s) {
    ans = "";
    unordered_map<char, unordered_set<char>> adj;

    // Build adjacency information
    for (int ix = 0; ix < s.size(); ix++) {
        char c = s[ix];
        if (adj.find(c) == adj.end()) {
            adj[c] = unordered_set<char>();
        }
        if (ix > 0) {        // s = '_aaaabded_' 일때 _ 에 해당하는 경우는 옆의 하나만 추가 
            adj[c].insert(s[ix - 1]);
        }
        if (ix < s.size() - 1) {
            adj[c].insert(s[ix + 1]);
        }
    }

    // for (auto cur:adj){
    //     cout << "key: " << cur.first << " value: " ;
    //     for (auto elem: cur.second){
    //         cout << elem << " ";
    //     }
    //     cout << '\n';
    // }

    // {'element': 1} dictionary  
    unordered_map<char, int> cnt;

    // Count occurrences of characters
    for (char c : s) {
        if (cnt.find(c) == cnt.end()) {
            cnt[c] = 1;
        }
    }

    // for (auto cur: cnt){
    //     cout << "first: " << cur.first << " second: " << cur.second << '\n';
    // }

    vector<char> buf;
    func(cnt, 0, buf, adj);

    if (s.size() == ans.size()){
        return ans; 
    }
    else{
        return "";
    }

    // return ans;
}

int main() {

    string s = "abcdcef"; 
    cout << foo(s) << '\n'; // accfbde
    cout << bar(s) << '\n'; // ""

    string t = "abcde";
    cout << foo(t) << '\n'; // acebd
    cout << bar(t) << endl; // bdace
    return 0; 
}
