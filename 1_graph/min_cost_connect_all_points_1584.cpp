// Kruskal's algorithm based on the Union-Find data structure 
/*
input: (x, y) 의 2-d points를 가진 array points 

조건: 두 포인트 사이의 거리는 manhattan distance |x_i - x_j| + |y_i - y_j|

output: the minimum cost to make all points connected  

*/


#include <queue> //queue 
#include <vector> //vector
#include <cmath> // abs function
#include <iostream> // cout 
#include <array> //array 

using namespace std;


class Solution {
public:
    int find(vector<int> &ds, int i) {
		// (bool) ? a: b
		// parent가 0보다 작으면 i를, 아니면 recursive하게 parent를 찾아라.  
        return ds[i] < 0 ? i : ds[i] = find(ds, ds[i]);
    }
    
    // 이 때 int은 점의 index i. 즉, ps[0] 하면 0번째 점이고 그 안에 (1,5) 같은 식으로 있는 건가? 
    // [ [0, 1], [1, 2], [2, 9] ...   ]
    int minCostConnectPoints(vector<vector<int>>& ps) {
        int n = ps.size(), res = 0;
        vector<int> ds(n, -1); // parent를 담는 list
        vector<array<int, 3>> arr; // array를 초기화할때는 array<data type,  (고정) 길이> 
        for (auto i = 0; i < n; ++i)
            for (auto j = i + 1; j < n; ++j) {
                arr.push_back({abs(ps[i][0] - ps[j][0]) + abs(ps[i][1] - ps[j][1]), i, j});
            }

        make_heap(begin(arr), end(arr), greater<array<int, 3>>()); // min-heap
        while (!arr.empty()) {
            pop_heap(begin(arr), end(arr), greater<array<int, 3>>()); // 맨 앞의 원소가 맨 뒤로 간다. 
            // auto [dist, i, j] = arr.back();
            int dist = arr.back()[0];  
            int i = arr.back()[1];   
            int j = arr.back()[2];  
  
            arr.pop_back(); // 맨 뒤 원소를 제거 
            i = find(ds, i), j = find(ds, j);
            if (i != j) {
                res += dist;
                ds[i] += ds[j]; // ? 
                ds[j] = i; // parent update 
                if (ds[i] == -n) // ? 
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