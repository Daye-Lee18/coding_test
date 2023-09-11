/*
MST(MSF) 를 찾는 방법 
모든 edge를 돌면서 cycle를 이루지 않는 가장 작은 weight을 가진 edge를 tree (forest)에 넣는다. 

- 기존 graph 의 edge들을 weight 오름차순 순서대로 나열하고 그 순서대로 돌면서 체크한다. (c++은 <algorithm>의 sort를 사용)
- disjoint struct의 constructor를 통해 자기 자신만 member로 가진 set를 initiation 
- disjoint struct의 find-set(x) -> parent를 찾는 함수
- disjoint struct의 union(x, y) -> 두 disjoint set을 연결시켜 parent를 update하는 함수 



*/

// C++ program for Kruskal's algorithm to find Minimum
// Spanning Tree of a given connected, undirected and weighted graph
#include <iostream> // cout
#include <vector>
#include <utility> //pair

using namespace std;

// Creating shortcut for an integer pair
typedef pair<int, int> iPair;

// Structure to represent a graph
struct Graph
{
	int V, E;
	vector< pair<int, iPair> > edges;

	// Constructor
	Graph(int V, int E){
		this->V = V;
		this->E = E;
	}

	// Utility function to add an edge
	void addEdge(int u, int v, int w){
	    // edges.push_back(make_pair(w, make_pair(u, v)));
		edges.push_back({w, {u, v}});
	}

	// Function to find MST using Kruskal's
	// MST algorithm
	int kruskalMST();
};

// To represent Disjoint Sets, 아래 두 함수를 포함함 
// find 함수 (disjoint set에서의 parent)
// merge 함수 (두 set을 합칠 때 rank를 비교하여 두 tree를 합친다. tree 상 depth가 누가 더 큰지 비교하기 위해 만든 것)
struct DisjointSets
{
	int *parent, *rnk;
	int n;

	// Constructor.
	DisjointSets(int n){
		// Allocate memory
		this->n = n;
		parent = new int[n+1];
		rnk = new int[n+1];

		// Initially, all vertices are in
		// different sets and have rank 0.
		for (int i = 0; i <= n; i++)
		{
			rnk[i] = 0;

			//every element is parent of itself
			parent[i] = i;
		}
	}

	// Find the parent of a node 'u'
	// Path Compression
	int find(int u)
	{
		/* Make the parent of the nodes in the path
		from u--> parent[u] point to parent[u] */
		if (u != parent[u])
			parent[u] = find(parent[u]);
		return parent[u];
	}

	// Union by rank, parent update 
	void merge(int x, int y)
	{
		x = find(x), y = find(y);

		/* Make tree with smaller height
		a subtree of the other tree */
		if (rnk[x] > rnk[y])
			parent[y] = x;
		else // If rnk[x] <= rnk[y]
			parent[x] = y;

		if (rnk[x] == rnk[y])
			rnk[y]++;
	}
};

/* Functions returns weight of the MST*/

int Graph::kruskalMST()
{
	int mst_wt = 0; // Initialize result

	// Sort edges in increasing order on basis of cost
  // (w, (u, v)) 순으로 edges에 들어있어서 제일 앞에 있는 w 으로 오름차순 
	sort(edges.begin(), edges.end());

	// Create disjoint sets
	DisjointSets ds(V);

	// Iterate through all sorted edges
	vector< pair<int, iPair> >::iterator it;
	for (it=edges.begin(); it!=edges.end(); it++)
	{ 
    // it -> first는 edge 의 weight 
		int u = it->second.first;
		int v = it->second.second;

		int set_u = ds.find(u);
		int set_v = ds.find(v);

		// Check if the selected edge is creating
		// a cycle or not (Cycle is created if u
		// and v belong to same set)
		if (set_u != set_v)
		{
			// Current edge will be in the MST
			// so print it
			cout << u << " - " << v << endl;

			// Update MST weight
			mst_wt += it->first;

			// Merge two sets
			ds.merge(set_u, set_v); // parent 를 업데이트 해줌 
		}
	}

	return mst_wt;
}

// Driver program to test above functions
int main()
{
	/* Let us create above shown weighted
	and undirected graph */
	int V = 9, E = 14;
	Graph g(V, E);

	// making above shown graph
	g.addEdge(0, 1, 4);
	g.addEdge(0, 7, 8);
	g.addEdge(1, 2, 8);
	g.addEdge(1, 7, 11);
	g.addEdge(2, 3, 7);
	g.addEdge(2, 8, 2);
	g.addEdge(2, 5, 4);
	g.addEdge(3, 4, 9);
	g.addEdge(3, 5, 14);
	g.addEdge(4, 5, 10);
	g.addEdge(5, 6, 2);
	g.addEdge(6, 7, 1);
	g.addEdge(6, 8, 6);
	g.addEdge(7, 8, 7);

	cout << "Edges of MST are \n";
	int mst_wt = g.kruskalMST();

	cout << "\nWeight of MST is " << mst_wt;

	return 0;
}




// #include <iostream>
// #include <vector>
// #include <algorithm> // sort 

// using namespace std;

// class Edge {
// public:
//     int src, dest, weight;

//     Edge(int src, int dest, int weight) {
//         this->src = src; // member variable이랑 parameter와 이름이 비슷해서 this을 이용해 구분해준 것 
//         this->dest = dest;
//         this->weight = weight;
//     }
// };

// class Graph {
//     int V;  // Number of vertices
//     vector<Edge> edges;

// public:
//     Graph(int V);
//     void addEdge(int src, int dest, int weight);
//     vector<Edge> kruskalMST(); // vecotr: push_back (emplace_back), pop_back, insert, size, empty, clear, front, back, begin, end 
// };

// Graph::Graph(int V) {
//     this->V = V;
// }

// void Graph::addEdge(int src, int dest, int weight) {
//     edges.emplace_back(src, dest, weight);
// }

// //Edge 클래스는 src, dest, weight의 member variable이 있지만, 그 중 weight 에 의해 ascending하게 sort할 compare 함수를 생성 
// bool compareEdges(const Edge& a, const Edge& b) {
//     return a.weight < b.weight;
// }

// // Function to find the parent of a vertex (uses the union-find algorithm)
// int findParent(vector<int>& parent, int v) {
//     if (parent[v] == v)
//         return v;
//     return findParent(parent, parent[v]);
// }

// // Function to perform union of two sets of vertices (uses the union-find algorithm)
// void unionSets(vector<int>& parent, int v1, int v2) {
//     int parent1 = findParent(parent, v1);
//     int parent2 = findParent(parent, v2);
//     parent[parent1] = parent2;
// }

// vector<Edge> Graph::kruskalMST() {
//     sort(edges.begin(), edges.end(), compareEdges); // vector<Edge>가 들은 edges들을 edge의 weight에 의해 ascending 순서로 나열, kruskal에서는 edge들을 minimum weight edge들을 순서대로 돌기 때문
//     vector<Edge> result;

//     vector<int> parent(V, -1); // parent에는 vertex의 개수만큼 -1로 initialziation을 해줌 

    
//     for (const Edge& edge : edges) { // const 는 edge parameter를 해당 kruskalMST 함수내에서 modify하지 못하게끔 하고 (edge를 read-only parameter)변환 Edge& (reference)를 넘김으로써 또다른 copy를 만들지 않고 memory에 직접 가서 modify하게끔 한다. 
//         int srcParent = findParent(parent, edge.src);
//         int destParent = findParent(parent, edge.dest);

//         if (srcParent != destParent) { // cycle 을 이루는지 확인 
//             result.push_back(edge);   // include the edge in the MST 
//             // parent[edge.dest] = edge.src;  // Union
//             unionSets(parent, srcParent, destParent);
//         }
//     }

//     return result;
// }

// int main() {
//     int V = 5;  // Number of vertices
//     Graph g(V);

//     // Adding edges to the graph
//     g.addEdge(0, 1, 2);
//     g.addEdge(0, 3, 6);
//     g.addEdge(1, 2, 3);
//     g.addEdge(1, 3, 8);
//     g.addEdge(1, 4, 5);
//     g.addEdge(2, 4, 7);
//     g.addEdge(3, 4, 9);

//     vector<Edge> mst = g.kruskalMST();

//     cout << "Minimum Spanning Tree Edges:" << endl;
//     for (const Edge& edge : mst) {
//         cout << edge.src << " - " << edge.dest << " (Weight: " << edge.weight << ")" << endl;
//     }

//     return 0;
// }