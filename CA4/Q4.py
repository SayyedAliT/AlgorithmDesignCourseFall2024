class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1
            return True
        return False

def kruskal_with_mandatory_edges(n, edges, mandatory_edges):
    uf = UnionFind(n)
    mst_cost = 0

    # First add all mandatory edges to the union-find structure
    for u, v, w in mandatory_edges:
       if uf.union(u, v):
            mst_cost += w
       else:
            return "NO"

    # Sort the remaining edges by weight
    copy_edge = edges.copy()
    copy_edge.sort(key=lambda x: x[2])

    # Add the remaining edges while checking for cycles and accumulating cost
    for u, v, w in copy_edge:
        if uf.union(u, v):
            mst_cost += w

    return mst_cost

def can_include_bridges(n, m, edges, queries):
    # Step 1: Compute initial MST cost with all edges
    initial_mst_cost = kruskal_with_mandatory_edges(n, sorted(edges, key=lambda x: x[2]), [])

    results = []

    for query in queries:
        k_i = query[0]
        requested_bridges_indices = query[1:k_i + 1]

        # Create a list of requested edges
        requested_edges = [(edges[idx - 1][0], edges[idx - 1][1], edges[idx - 1][2]) for idx in requested_bridges_indices]

        # Create a list of remaining edges
        remaining_edges = [edges[i] for i in range(m) if (i + 1) not in requested_bridges_indices]

        # Step 3: Run Kruskal's algorithm on combined edges to get new MST cost with mandatory edges
        new_mst_cost = kruskal_with_mandatory_edges(n, remaining_edges, requested_edges)

        # Step 4: Compare costs with initial MST cost
        if new_mst_cost == initial_mst_cost:
            results.append("YES")
        else:
            results.append("NO")

    return results

# Input Handling
def main():
    # Read number of islands and bridges
    n, m = map(int, input().split())

    edges = []

    # Read the bridges information
    for _ in range(m):
        u, v, w = map(int, input().split())
        edges.append((u - 1, v - 1, w))  # Convert to zero-indexed

    # Read number of queries
    q = int(input())

    queries = []

    # Read each query
    for _ in range(q):
        query_data = list(map(int, input().split()))
        queries.append(query_data)

    # Function Call to get results
    results = can_include_bridges(n, m, edges, queries)

    # Print results for each query
    print("\n".join(results))

if __name__ == "__main__":
    main()
