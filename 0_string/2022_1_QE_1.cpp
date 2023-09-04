#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <unordered_set>

using namespace std;

bool is_palindrome(const string& s) {
    int len_s = s.size();
    int mid = len_s / 2;
    int l;
    int r;

    if (len_s % 2 == 0) {
        l = mid - 1;
        r = mid;
    } else {
        l = r = mid;
    }

    while (l >= 0 && r < len_s && s[l] == s[r]) {
        l -= 1;
        r += 1;
    }
    
    return (l == -1) ? true : false;
}

// int main(){
//     string s = "my";
//     string k = "mystring";
//     string d = "d";
//     string e = " ";
//     string a = "qwerreq";
//     cout << is_palindrome(s) << " ";
//     cout << is_palindrome(k) << " ";
//     cout << is_palindrome(d) << " ";
//     cout << is_palindrome(e) << " ";
//     cout << is_palindrome(a) << " ";
    
//     return 0;
// }

bool substring(const string& s, const string& t) {
    int len_s = s.size();
    int len_t = t.size();

    if (len_s < len_t) {
        return false;
    }

    for (int i = 0; i <= len_s - len_t; ++i) {
        if (s.substr(i, len_t) == t) {
            return true;
        }
    }

    return false;
}

vector<string> max_palindrome(const string& s) {
    // find all palindromes 
    //vector<string> temp;
    unordered_set<string> temp;
    for (int i = 0; i < s.size(); i++){
        for (int j = i+1; j < s.size(); j++){
            string candidate = s.substr(i,j);
            if (is_palindrome(candidate)){
                temp.insert(candidate);
            }
        }
    }
    
    //make set into vector 
    vector<string> target;
    for (const auto&it: temp){
        target.push_back(it);
    }
    
    // for (string _:target){
    //     cout << _ << " ";
    // }
    // cout << '\n';
    
    // remove redundant substring 
    sort(target.begin(), target.end(), [](const string &s, const string& t){
        return s.size() < t.size();
    });
    
    vector<string> ans;
    
    for (int i = 0; i <target.size(); i++){
        bool is_redundant = false;
        for (int j = i+1; j <target.size()+1; j++){
            if (substring(target[j], target[i])){
                is_redundant = true;
                break;
            }
        }
        if (!is_redundant){
            ans.push_back(target[i]);
        }
    }
    
    return ans;
}
int main() {
    string s = "kabccba dzabccbaza";
    
    vector<string> result = max_palindrome(s);

    for (const string& palindrome : result) {
        cout << palindrome << " "; // ["k", " ", "d", "zabccbaz", "aza"]
    }

    return 0;
}

