#include <vector>
#include <unordered_map>
#include <iostream>
#include <unordered_set> 

using namespace std;

class Solution {
public:
    vector<int> findMinHeightTrees(int n, vector<vector<int>>& edges) {
        if (n ==1 || edges.empty()){
            return {0}; // return 값이 vector<int>이니까 이를 {}를 통해 initialization해주면서 return 됨
        }

        vector<int> ans;
        unordered_map<int, unordered_set<int>> graph; 

        for (const vector<int>& edge : edges){
            const int u = edge[0];
            const int v = edge[1];
            graph[u].insert(v); // c++은 미리 graph[i]의 data type을 unordered_set으로 해두어서 python과 다르게 처음 보나 두번째 보는 것이나 insert로 하면된다 
            graph[v].insert(u);
        }

        // unordered_map을 iterating하는 방법 
        // for (pair<int, unordered_set<int>> next:graph){
        //     int key = next.first;
        //     unordered_set<int> value = next.second;
        // }

        // 마지막에 노드가 남을 때까지 리프노드를 제거해나간다. 
        // 해당 엣지가 리프노드라면 리스트의 길이가 1이므로 리프노드를 걸러낸다. 
        for (const auto& [label, children]: graph){ // ? 
            if (children.size() == 1){
                ans.push_back(label);
            }
        }

        while (n>2){
            n -= ans.size();
            vector<int> nextLeaves;
            for (const int leaf: ans){
                const int u = *graph[leaf].begin(); // graph[leaf].begin() iterator를 dereferencing 
                graph[u].erase(leaf);
                if (graph[u].size() == 1){
                    nextLeaves.push_back(u);
                }
            }
            ans = nextLeaves;
        }

        return ans;
    }
};