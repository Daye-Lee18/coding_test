// Kruskal's algorithm based on the Union-Find data structure 
#include <queue> //queue 
#include <vector> //vector
#include <cmath> // abs function
#include <iostream> // cout 
#include <array> //array 

using namespace std;

// // Union-Find = Disjoint Set Union 
// class UnionFind {
//     vector<int> parent;  
//     vector<int> rank;  
// public:
//     UnionFind(int n) {
//         rank.resize(n);
//         parent.resize(n);

//         for (int i = 0; i < n; i++) parent[i] = i; // 각 element의 parent를 자기 자신으로 initialization해주고 component를 update할때마다 parent를 update해준다. 
//     }
//     // finds the representative (root) of a component and performs path compression to improve efficiency 
//     int find(int x) {
//         if (parent[x] != x) {
//             parent[x] = find(parent[x]);
//         }
//         return parent[x];
//     }
    
//     // performs a union of two components by attaching the component with the lower rank to the one with the higher rank 
//     bool uni(int x, int y) {  
//         int parentX = find(x);
//         int parentY = find(y);
//         if (parentX == parentY) return false; // node x, y가 이미 같은 component에 있다면 x와 y를 연결하는 tree를 만들면 cycle을 형성하므로 false를 벹음 
//         if (rank[parentX] == rank[parentY]) {
//             parent[parentX] = parentY;
//             rank[parentY] += 1;
//         } else if (rank[parentX] < rank[parentY]) {
//             parent[parentX] = parentY;
//         } else {
//             parent[parentY] = parentX;
//         }
//         return true;
//     }
// };

// class Solution {
// public:
//     int minCostConnectPoints(vector<vector<int>>& points) {  
//         if (points.empty() || points.size() == 0) return 0;

//         priority_queue<vector<int>, vector<vector<int>>, greater<vector<int>>> heap; //min-heap 

//         // min-heap에 각 포인트들간의 distance를 저장한다. (kruskal의 sort와 비슷) 
//         for (int i = 0; i < points.size() - 1; i++) {
//             for (int j = i + 1; j < points.size(); j++) {
//                 heap.push({distance(points, i, j), i, j});  
//             }
//         }

//         int minCost = 0;
//         UnionFind uf(points.size());  
//         while (!heap.empty()) {  
//             vector<int> edge = heap.top(); heap.pop();  
//             if (uf.uni(edge[1], edge[2])) {  // cycle을 이루지 않으면, 
//                 minCost += edge[0];
//             }
//         }

//         return minCost;
//     }

//     int distance(vector<vector<int>>& points, int a, int b) { 
//         return abs(points[a][0] - points[b][0]) + abs(points[a][1] - points[b][1]);
//     }
// };

class Solution {
public:
    int find(vector<int> &ds, int i) {
		// (bool) ? a: b
		// parent가 0보다 작으면 i를, 아니면 recursive하게 parent를 찾아라.  
        return ds[i] < 0 ? i : ds[i] = find(ds, ds[i]);
    }
    
    int minCostConnectPoints(vector<vector<int>>& ps) {
        int n = ps.size(), res = 0;
        vector<int> ds(n, -1); // parent를 담는 list
        vector<array<int, 3>> arr;
        for (auto i = 0; i < n; ++i)
            for (auto j = i + 1; j < n; ++j) {
                arr.push_back({abs(ps[i][0] - ps[j][0]) + abs(ps[i][1] - ps[j][1]), i, j});
            }

        make_heap(begin(arr), end(arr), greater<array<int, 3>>());
        while (!arr.empty()) {
            pop_heap(begin(arr), end(arr), greater<array<int, 3>>());
            // auto [dist, i, j] = arr.back();
            int dist = arr.back()[0];
            int i = arr.back()[1];
            int j = arr.back()[2];

            arr.pop_back();
            i = find(ds, i), j = find(ds, j);
            if (i != j) {
                res += dist;
                ds[i] += ds[j];
                ds[j] = i;
                if (ds[i] == -n)
                    break;
            }
        }
        return res;
    }
};

int main(){
    vector<vector<int>> points (5);
    vector<int> point1 = {0,0};
    vector<int> point2 = {2,2};
    vector<int> point3 = {3,10};
    vector<int> point4 = {5,2};
    vector<int> point5 = {7,0};

    points.push_back(point1);
    points.push_back(point2);
    points.push_back(point3);
    points.push_back(point4);
    points.push_back(point5);

    // for (auto it = points.begin(); it != points.end(); it++){
        
    //     // std::cout << it[1] << it[2] ;
    //     for (int num:*it){
    //         cout << num << " ";
    //     }

    //     cout << '\n';
    // }

    Solution x;

    int minCost = x.minCostConnectPoints(points);

    cout << "This is the minCost: " ;
    cout << minCost;

    return 0;
}