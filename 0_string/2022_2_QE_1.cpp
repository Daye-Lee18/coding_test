// Online C++ compiler to run C++ program online
#include <iostream>
#include <string>
#include <vector>
#include <algorithm> // sort 
#include <unordered_set>

using namespace std;

// input based recursion 
void permute(vector<char> & input, int l, int r, unordered_set<string>& output){
    //based case 
    // for (auto _: input){
    //     output.push_back(_);
    // }
    
    if (l == r){
        
        string result(input.begin(), input.end());
        // cout << '"' << result << '"'<< " ";
        output.insert(result);
    }
    
    for (int i =l; i <r;i++){
        // swap
        char cur = input[l];
        input[l] = input[i];
        input[i] = cur;
        
        // recursion call 
        permute(input, l+1, r, output);
        
        // swap
        cur = input[l];
        input[l] = input[i];
        input[i] = cur;
    }
}

vector<string> str_perms(string s){
    unordered_set<string> output;
    
    // make s into vector<char> 
    vector<char> input;
    for (auto _ : s){
        input.push_back(_);
    }
    
    permute(input, 0, s.size(), output); // input based recursion 
    
    //change set into vector 
    vector<string> v(output.begin(), output.end());
    
    //sort output (char순서대로 sorting)
    sort(v.begin(), v.end(), [](const string& a, const string &b){
        return a <= b;});
    
    return v;
}

int main(){
    string a = "ABC";
    vector<string> output = str_perms(a);
    
    for (auto _: output){
        cout << _ << " ";
    }
    
    return 0;
}