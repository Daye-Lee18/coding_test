/*
start와 dest가 있는 상황에서, shortest path 를 찾는 과정 
negative wieght이 없는 상황에서 사용 

모든 vertex를 돌면서 해당 VERTEX에 연결된 edge에 대해 relaxation한다.

- priority queue를 사용한다. 

 pseudo code 
 
 1  function Dijkstra(Graph, source):
 2      
 3      for each vertex v in Graph.Vertices:
 4          dist[v] ← INFINITY
 5          prev[v] ← UNDEFINED
 6          add v to Q
 7      dist[source] ← 0
 8      
 9      while Q is not empty:
10          u ← vertex in Q with min dist[u]
11          remove u from Q
12          
13          for each neighbor v of u still in Q:
14              alt ← dist[u] + Graph.Edges(u, v) // alt = the length of the path from the root node to the neighbor node v if it were to go through u 
15              if alt < dist[v]:
16                  dist[v] ← alt
17                  prev[v] ← u
18
19      return dist[], prev[]


*/

// Program to find Dijkstra's shortest path using
// priority_queue in STL
#include <utility>
#include <iostream>
#include <vector>
#include <queue>
#include <climits> // INT_MAX

using namespace std;


// iPair ==> Integer Pair
typedef pair<int, int> iPair;

// To add an edge
// adj란 array가 argument로 들어온다.  
void addEdge(vector<iPair> adj[], int u, int v,
			int wt)
{
	adj[u].push_back(make_pair(v, wt));
	adj[v].push_back(make_pair(u, wt));
}

// Prints shortest paths from src to all other vertices
void shortestPath(vector<pair<int, int> > adj[], int V,
				int src)
{
	// Create a priority queue to store vertices that are being preprocessed. 
	priority_queue<iPair, vector<iPair>, greater<iPair> > pq; // distance, vertex 가 pair로 저장됨 
	vector<int> dist(V, INT_MAX); // Create a vector for distances and initialize all distances as infinite (INF)
	
	pq.push(make_pair(0, src)); // Insert source itself in priority queue and initialize its distance as 0.
	dist[src] = 0;

	/* Looping till priority queue becomes empty (or all distances are not finalized) */
	while (!pq.empty()) {
		int u = pq.top().second;
		pq.pop();

		// Get all adjacent of u.
		for (auto x : adj[u]) {
			// Get vertex label and weight of current
			// adjacent of u.
			int v = x.first;
			int weight = x.second;

			// If there is shorted path to v through u.
			if (dist[v] > dist[u] + weight) {
				// Updating distance of v
				dist[v] = dist[u] + weight;
				pq.push(make_pair(dist[v], v)); // relaxation 된 node를 pq에 넣음 
			}
		}
	}

	// Print shortest distances stored in dist[]
	printf("Vertex Distance from Source\n");
	for (int i = 0; i < V; ++i)
		printf("%d \t\t %d\n", i, dist[i]);
}

// Driver program to test methods of graph class
int main()
{
	int V = 9;
	vector<iPair> adj[V];

	// making above shown graph
	addEdge(adj, 0, 1, 4);
	addEdge(adj, 0, 7, 8);
	addEdge(adj, 1, 2, 8);
	addEdge(adj, 1, 7, 11);
	addEdge(adj, 2, 3, 7);
	addEdge(adj, 2, 8, 2);
	addEdge(adj, 2, 5, 4);
	addEdge(adj, 3, 4, 9);
	addEdge(adj, 3, 5, 14);
	addEdge(adj, 4, 5, 10);
	addEdge(adj, 5, 6, 2);
	addEdge(adj, 6, 7, 1);
	addEdge(adj, 6, 8, 6);
	addEdge(adj, 7, 8, 7);

	shortestPath(adj, V, 0);

	return 0;
}
