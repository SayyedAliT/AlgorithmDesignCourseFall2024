#include <iostream>
#include <vector>
#include <tuple>
#include <set>
#include <algorithm>
#include <limits> // For INT_MAX

using namespace std;

class UnionFind {
public:
    vector<int> parent, rank;

    UnionFind(int n) {
        parent.resize(n);
        rank.resize(n, 0);
        for (int i = 0; i < n; ++i) {
            parent[i] = i;
        }
    }

    int find(int u) {
        if (parent[u] != u) {
            parent[u] = find(parent[u]); // Path compression
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
};

int kruskalWithMandatoryEdges(int n, const vector<tuple<int, int, int>>& edges, const vector<tuple<int, int, int>>& mandatoryEdges) {
    UnionFind uf(n);
    int mstCost = 0;
    int addedEdges = 0;

    // Add mandatory edges first
    for (auto [u, v, w] : mandatoryEdges) {
        if (uf.unionSets(u, v)) {
            mstCost += w;
            addedEdges++;
        } else {
            return INT_MAX; // Return infinity if a cycle is detected
        }
    }

    // Add remaining edges to complete the MST
    for (auto [u, v, w] : edges) {
        if (addedEdges == n - 1) break; // Stop if we already have a spanning tree
        if (uf.unionSets(u, v)) {
            mstCost += w;
            addedEdges++;
        }
    }

    return (addedEdges == n - 1) ? mstCost : INT_MAX;
}

vector<string> canIncludeBridges(int n, int m, vector<tuple<int, int, int>>& edges, vector<vector<int>>& queries) {
    vector<string> results;
    sort(edges.begin(), edges.end(), [](auto& a, auto& b) {
        return get<2>(a) < get<2>(b); // Sort edges by weight
    });

    // Compute the initial MST cost with all edges
    int initialMstCost = kruskalWithMandatoryEdges(n, edges, {});

    for (auto& query : queries) {
        int k_i = query[0];
        vector<tuple<int, int, int>> mandatoryEdges;
        set<int> requestedIndices(query.begin() + 1, query.end());

        // Create a list of mandatory edges
        for (int idx : requestedIndices) {
            mandatoryEdges.push_back(edges[idx - 1]); // Convert 1-indexed to 0-indexed
        }

        // Create a list of remaining edges
        vector<tuple<int, int, int>> remainingEdges;
        for (int i = 0; i < m; ++i) {
            if (requestedIndices.find(i + 1) == requestedIndices.end()) {
                remainingEdges.push_back(edges[i]);
            }
        }

        // Run Kruskal's algorithm
        int newMstCost = kruskalWithMandatoryEdges(n, remainingEdges, mandatoryEdges);

        // Compare costs with the initial MST cost
        results.push_back((newMstCost == initialMstCost) ? "YES" : "NO");
    }

    return results;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    cin >> n >> m;

    vector<tuple<int, int, int>> edges;
    for (int i = 0; i < m; ++i) {
        int u, v, w;
        cin >> u >> v >> w;
        edges.emplace_back(u - 1, v - 1, w); // Convert to zero-indexed
    }

    int q;
    cin >> q;

    vector<vector<int>> queries(q);
    for (int i = 0; i < q; ++i) {
        int k;
        cin >> k;
        queries[i].resize(k + 1);
        queries[i][0] = k;
        for (int j = 1; j <= k; ++j) {
            cin >> queries[i][j];
        }
    }

    vector<string> results = canIncludeBridges(n, m, edges, queries);
    for (const string& res : results) {
        cout << res << "\n";
    }

    return 0;
}
