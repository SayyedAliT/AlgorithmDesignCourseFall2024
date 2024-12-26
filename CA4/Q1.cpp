#include <iostream>
#include <vector>
#include <unordered_set>
#include <unordered_map>
using namespace std;

void explore_graph(int vertex, unordered_map<int, unordered_set<int>>& graph, unordered_set<int>& visited) {
    visited.insert(vertex);
    for (int neighbor : graph[vertex]) {
        if (visited.find(neighbor) == visited.end()) {
            explore_graph(neighbor, graph, visited);
        }
    }
}

bool check_connectivity(int n, const vector<pair<int, int>>& edges) {
    if (edges.empty()) {
        return false;
    }

    // Create adjacency list
    unordered_map<int, unordered_set<int>> graph;
    for (const auto& edge : edges) {
        int start = edge.first;
        int end = edge.second;
        graph[start].insert(end);
        graph[end].insert(start);
    }

    // Start DFS from the first vertex (assuming vertices are 1-indexed)
    unordered_set<int> visited;
    int start_vertex = 1;
    explore_graph(start_vertex, graph, visited);

    // Check if all vertices were visited
    return visited.size() == n;
}

void solve() {
    int n, m;
    cin >> n >> m;
    vector<pair<int, int>> edge_list;

    for (int i = 0; i < m; ++i) {
        int u, v;
        cin >> u >> v;
        edge_list.push_back({u, v});
    }

    // Basic checks
    if (m < n - 1 || n <= 1) {
        cout << 0 << endl;
        return;
    }

    // Check connectivity and print result
    if (check_connectivity(n, edge_list)) {
        cout << n - 1 << endl;
    } else {
        cout << 0 << endl;
    }
}

int main() {
    solve();
    return 0;
}
