/*
prim
    - MST를 찾고 싶을 때, 모든 vertex를 돌면서 각 vertex에 연결된 edge 중 
        weight이 가장 작은 edge를 tree에 더해준다. 
    - vertex를 돌 때 tree에 대해준 edge의 destination node를 그 다음에 돌게 된다.  
*/


#include <iostream>
#include <vector>   // vector 
#include <queue>   // priority_queue 
#include <climits> // INT_MAX

using namespace std;

typedef pair<int, int> pii;  // Pair of vertex and weight

class Graph {
    int V;  // Number of vertices
    vector<vector<pii>> adj;  // Adjacency list

public:
    Graph(int V);
    void addEdge(int u, int v, int w);
    void primMST();
};

Graph::Graph(int V) {
    this->V = V;
    adj.resize(V);
}

// adj[current node] 는 (연결된 노드, weight) 를 저장해둠 
void Graph::addEdge(int u, int v, int w) {
    
    // emplace_back(int, int) 로 사용가능하지만, push_back(item((int, int))) 이런식으로 사용해야 한다. 
    // emplace_back()은 vector<vector<int, int>> 와 같은 구조에, push_back()은 vector<int>에 사용 
    // adj[u] 는 pair를 element로 가지므로 [[(v,w) ..], [()...]] 그 pair object를 생성할 때 필요한 constructor argument를 emplce_back안에 넣어주면 pair object가 생성 및 adj[u]에 추가됨 
    adj[u].emplace_back(v, w); // emplace_back = push_back과 동일 (내부적인 작동방식이 다른데, https://openmynotepad.tistory.com/10 참고 )
    adj[v].emplace_back(u, w);
}

// parent 에 MST를 저장할것
void Graph::primMST() {
    priority_queue<pii, vector<pii>, greater<pii>> pq;  // Min-heap
    vector<int> key(V, INT_MAX);  // Key values to track minimum edge weights, key[v]는 기존 weight를 저장 
    vector<int> parent(V, -1);  // Parent array to store MST

    int src = 0;  // Start from vertex 0
    pq.push(make_pair(0, src)); // pq는 (initial weight, vertex) 를 저장 
    key[src] = 0;

    while (!pq.empty()) {
        int u = pq.top().second;
        pq.pop();

        for (const auto& neighbor : adj[u]) {
            int v = neighbor.first;
            int weight = neighbor.second;
            
            // key[v]는 기존 weight를 저장, weight은 현재 노드와 연결된 edge의 weight 
            if (key[v] > weight) {
                pq.push(make_pair(weight, v));
                key[v] = weight;
                parent[v] = u;
            }
        }
    }

    // Print the MST edges
    cout << "Minimum Spanning Tree:" << endl;
    for (int i = 1; i < V; ++i) {
        cout << parent[i] << " - " << i << endl;
    }
}

int main() {
    int V = 5;  // Number of vertices
    Graph g(V);

    // Adding edges to the graph
    g.addEdge(0, 1, 2);
    g.addEdge(0, 3, 6);
    g.addEdge(1, 2, 3);
    g.addEdge(1, 3, 8);
    g.addEdge(1, 4, 5);
    g.addEdge(2, 4, 7);
    g.addEdge(3, 4, 9);

    g.primMST();

    return 0;
}