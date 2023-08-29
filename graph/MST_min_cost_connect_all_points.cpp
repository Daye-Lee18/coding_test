// Prim's Kruskals' algorithm based on the Union-Find data structure 
#include <queue>
#include <vector>
#include <cmath> // abs function

using namespace std;

class Solution {
public:
    int minCostConnectPoints(vector<vector<int>>& points) {  // Changed 'vector<int>' to 'vector<vector<int>>&'
        if (points.empty() || points.size() == 0) return 0;

        priority_queue<vector<int>, vector<vector<int>>, greater<vector<int>>> heap;  // Used 'vector<int>' instead of 'int[]'

        for (int i = 0; i < points.size() - 1; i++) {
            for (int j = i + 1; j < points.size(); j++) {
                heap.push({distance(points, i, j), i, j});  // Changed 'new [int]' to '{...}'
            }
        }
        int minCost = 0;
        UnionFind uf(points.size());  // Used 'points.size()' instead of 'points.length'
        while (!heap.empty()) {  // Changed 'heap.isEmpty()' to '!heap.empty()'
            vector<int> edge = heap.top(); heap.pop();  // Used 'top()' and 'pop()' instead of 'poll()'
            if (uf.uni(edge[1], edge[2])) {  // Changed 'union' to 'uni'
                minCost += edge[0];
            }
        }

        return minCost;
    }

    int distance(vector<vector<int>>& points, int a, int b) {  // Changed 'int[][]' to 'vector<vector<int>>&'
        return abs(points[a][0] - points[b][0]) + abs(points[a][1] - points[b][1]);
    }
};

// Union-Find = Disjoint Set Union 
class UnionFind {
    vector<int> parent;  
    vector<int> rank;  
public:
    UnionFind(int n) {
        rank.resize(n);
        parent.resize(n);

        for (int i = 0; i < n; i++) parent[i] = i;
    }
    // finds the representative (root) of a component and performs path compression to improve efficiency 
    int find(int x) {
        if (parent[x] != x) {
            parent[x] = find(parent[x]);
        }
        return parent[x];
    }
    
    // performs a union of two components by attaching the component with the lower rank to the one with the higher rank 
    bool uni(int x, int y) {  
        int parentX = find(x);
        int parentY = find(y);
        if (parentX == parentY) return false;
        if (rank[parentX] == rank[parentY]) {
            parent[parentX] = parentY;
            rank[parentY] += 1;
        } else if (rank[parentX] < rank[parentY]) {
            parent[parentX] = parentY;
        } else {
            parent[parentY] = parentX;
        }
        return true;
    }
};
