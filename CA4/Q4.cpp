#include <iostream>
#include <vector>
#include <tuple>
#include <algorithm>
#include <numeric>
using namespace std;

class UnionFind {
public:
    UnionFind(int n) : parent(n), rank(n, 0) {
        iota(parent.begin(), parent.end(), 0); // Initialize parent to [0, 1, 2, ..., n-1]
    }

    int find(int u) {
        if (parent[u] != u) {
            parent[u] = find(parent[u]);
        }
        return parent[u];
    }

    bool unionSets(int u, int v) {
        int root_u = find(u);
        int root_v = find(v);
        if (root_u != root_v) {
            if (rank[root_u] > rank[root_v]) {
                parent[root_v] = root_u;
            } else if (rank[root_u] < rank[root_v]) {
                parent[root_u] = root_v;
            } else {
                parent[root_v] = root_u;
                rank[root_u]++;
            }
            return true;
        }
        return false;
    }

private:
    vector<int> parent;
    vector<int> rank;
};

int kruskalWithMandatoryEdges(int n, const vector<tuple<int, int, int>>& edges, const vector<tuple<int, int, int>>& mandatoryEdges) {
    UnionFind uf(n);
    int mst_cost = 0;

    // First add all mandatory edges to the union-find structure
    for (const auto& edge : mandatoryEdges) {
        int u = get<0>(edge);
        int v = get<1>(edge);
        int w = get<2>(edge);
        if (!uf.unionSets(u, v)) {
            return -1; // Cycle detected
        }
        mst_cost += w;
    }

    // Sort the remaining edges by weight
    vector<tuple<int, int, int>> sortedEdges = edges;
    sort(sortedEdges.begin(), sortedEdges.end(), [](const auto& a, const auto& b) {
        return get<2>(a) < get<2>(b);
    });

    // Add the remaining edges while checking for cycles and accumulating cost
    for (const auto& edge : sortedEdges) {
        int u = get<0>(edge);
        int v = get<1>(edge);
        int w = get<2>(edge);
        if (uf.unionSets(u, v)) {
            mst_cost += w;
        }
    }

    return mst_cost;
}

vector<string> canIncludeBridges(int n, int m, vector<tuple<int, int, int>>& edges, const vector<vector<int>>& queries) {
    vector<string> results;

    // Step 1: Compute initial MST cost with all edges
    int initial_mst_cost = kruskalWithMandatoryEdges(n, edges, {});

    for (const auto& query : queries) {
        int k_i = query[0];
        vector<int> requested_bridges_indices(query.begin() + 1, query.begin() + k_i + 1);

        // Create a list of requested edges
        vector<tuple<int, int, int>> requested_edges;
        for (int idx : requested_bridges_indices) {
            requested_edges.push_back(edges[idx - 1]);
        }

        // Check if requested edges form a cycle by themselves
        UnionFind uf_temp(n);
        bool valid_request = true;
        for (const auto& edge : requested_edges) {
            int u = get<0>(edge);
            int v = get<1>(edge);
            int w = get<2>(edge);
            if (!uf_temp.unionSets(u, v)) {
                valid_request = false;
                break;
            }
        }

        if (valid_request) {
            // Create a list of remaining edges
            vector<tuple<int, int, int>> remaining_edges;
            for (int i = 0; i < m; ++i) {
                if (find(requested_bridges_indices.begin(), requested_bridges_indices.end(), i + 1) == requested_bridges_indices.end()) {
                    remaining_edges.push_back(edges[i]);
                }
            }

            // Step 3: Run Kruskal's algorithm on combined edges to get new MST cost with mandatory edges
            int new_mst_cost = kruskalWithMandatoryEdges(n, remaining_edges, requested_edges);

            // Step 4: Compare costs with initial MST cost
            if (new_mst_cost == initial_mst_cost) {
                results.push_back("YES");
            } else {
                results.push_back("NO");
            }
        } else {
            results.push_back("NO");
        }
    }

    return results;
}

int main() {
    // Read number of islands and bridges
    int n, m;
    cin >> n >> m;

    vector<tuple<int, int, int>> edges(m);

    // Read the bridges information
    for (int i = 0; i < m; ++i) {
        int u, v, w;
        cin >> u >> v >> w;
        edges[i] = {u - 1, v - 1, w}; // Convert to zero-indexed
    }

    // Read number of queries
    int q;
    cin >> q;

    vector<vector<int>> queries(q);

    // Read each query
    for (int i = 0; i < q; ++i) {
        int k;
        cin >> k;
        queries[i].resize(k + 1);
        queries[i][0] = k;
        for (int j = 1; j <= k; ++j) {
            cin >> queries[i][j];
        }
    }

    // Function Call to get results
    vector<string> results = canIncludeBridges(n, m, edges, queries);

    // Print results for each query
    for (const auto& result : results) {
        cout << result << endl;
    }

    return 0;
}
