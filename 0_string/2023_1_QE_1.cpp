#include <iostream>
#include <vector>
#include <string> 
#include <unordered_map> // python의 dictionary find(key), count(key) ,insert({key, value}) erase(key), clear 
#include <unordered_set> // set used to store the adjacency list of a certain char 

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

// dfs recursion: input based recursion 
    
// void dfs(const unordered_map<char, unordered_set<char>>& adj, unordered_map<char, int>& Cnt, string& buffer, int &max_size, string& ans){
    
//     if (max_size == Cnt.size()){
//         string ans = buffer;
//         return ;
//     }

//     for (auto cur: adj){
//         if (Cnt[cur.first] > 0){
//             buffer += cur.first ;
//             Cnt[cur.first] -= 1;
//             max_size += 1;
//             dfs(adj, Cnt, buffer, max_size, ans);
//         }
//         else {
//             continue;
//         }
//     }
// }

void dfs(const unordered_map<char, unordered_set<char>>& adj, unordered_map<char, int>& Cnt, string& buffer, int &max_size, string& ans){
    
    if (max_size == Cnt.size()){
        string ans = buffer;
        return ;
    }

    for (auto cur: Cnt){
        auto it = adj.find(buffer.back()); // set을 가리키는 iterator 
        auto cur_set = *it;
        if (Cnt[cur.first] > 0 && cur_set.second.find(cur.first) == cur_set.second.end()){
            buffer += cur.first ;
            Cnt[cur.first] -= 1;
            max_size += 1;
            dfs(adj, Cnt, buffer, max_size, ans);
        }
        else {
            continue;
        }
    }
}

string bar(const string& s){
    // adj dictionary 
    unordered_map<char, unordered_set<char>> adj;

    int count = 0;
    for (char cur: s){
        
        if (count > 0 && count <= s.size() -2){
            unordered_set<char> cur_set;
            cur_set.insert(s[count-1]);
            cur_set.insert(s[count+1]);
            adj[cur] =  cur_set;
            count += 1 ;
        }
        else if (count == 0){
            unordered_set<char> cur_set;
            cur_set.insert(s[count+1]);
            adj[cur] = cur_set;
            count += 1 ;
        }
        else { // (count == s.size() -1)
            unordered_set<char> cur_set;
            cur_set.insert(s[count-1]);
            adj[cur] = cur_set;
            count += 1 ;
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
    
    unordered_map<char, int> Cnt;
    for (auto cur: adj){
        Cnt[cur.first] = 1;
    }


    // for (auto cur: Cnt){
    //     cout << "first: " << cur.first << " second: " << cur.second << '\n';
    // }
    

    string buf = "";
    int max_size = 0 ;
    string ans = "";

    // dfs recursion: input based recursion 
    dfs(adj, Cnt, buf, max_size, ans);

    if (max_size == s.size()){
        return ans;
    }
    else{
        return "";
    }

}

int main(){
    // string s = "abcdcef"; 
    // cout << foo(s) << '\n'; // accfbde
    // cout << bar(s) << '\n'; // ""

    string t = "abcde";
    cout << foo(t) << '\n'; // acebd
    cout << bar(t) << '\n'; // "adbec"
}