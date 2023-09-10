#include <vector>
#include <queue>
#include <climits>
#include <math>

using namespace std;

class Solution {
public:
    double maxProbability(int n, vector<vector<int>>& edges, vector<double>& succProb, int start, int end) {
    // declare graph object
		vector<vector<pair<int, double>>> graph(n);
		// add succProb relationship btw nodes to graph
    for (int i = 0; i < edges.size(); i++) {
        int a = edges[i][0];
        int b = edges[i][1];
				// log function applied for addition operation
        double w = -log(succProb[i]);
				// connect node a with b with Prob w
        graph[a].push_back({b, w});
				// connect node b with a with Prob w (무방향 간선)
        graph[b].push_back({a, w});
    }
		// declare dist find max
    vector<double> dist(n, numeric_limits<double>::max());
    dist[start] = 0;
		// priority queue(top:max) 
		// priority_queue < [Data Type], [Container Type], [정렬기준] > [변수이름];
    priority_queue<pair<double, int>, vector<pair<double, int>>, greater<>> heap; // (min-heap)
	  // push start node with dist 0  
		heap.push({0, start});
		// while not empty
    while (!heap.empty()) {
				// greedy access
        auto [d, u] = heap.top();
				// member function, no return value
        heap.pop();
				// pass when dist[u] are smaller than d
        if (d > dist[u]) {
            continue;
        }
				// for every node of graph 
        for (auto [v, w] : graph[u]) {
						// update distance when previous path values are smaller than dist[v]
            if (dist[v] > dist[u] + w) {
                dist[v] = dist[u] + w;
                heap.push({dist[v], v});
            }
        }
    }
		// return 0 when dist[end] is max else return og value (inverse of log is exp) 
    // dist[end]가 최대값이면 0을 반환하고, 그렇지 않으면 exp(-dist[end]) 값을 반환
		return dist[end] == numeric_limits<double>::max() ? 0 : exp(-dist[end]);
}

};