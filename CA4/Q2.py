from collections import deque

# Directions for moving in 4 directions (up, down, left, right)
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def bfs(start_positions, n, m, grid):
    # Distance from the numbered houses
    distances = [[float('inf')] * m for _ in range(n)]
    queue = deque()

    # Adding the numbered houses to the queue
    for x, y in start_positions:
        queue.append((x, y))
        distances[x][y] = 0

    while queue:
        x, y = queue.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] != '#' and distances[nx][ny] == float('inf'):
                distances[nx][ny] = distances[x][y] + 1
                queue.append((nx, ny))

    return distances

def min_distance_between_groups(start_positions_1, start_positions_2, n, m, grid):
    # BFS for each group
    dist_1 = bfs(start_positions_1, n, m, grid)
    dist_2 = bfs(start_positions_2, n, m, grid)

    # Finding the minimum distance between the groups
    min_distance = float('inf')
    for i in range(n):
        for j in range(m):
            if grid[i][j] == '.':
                min_distance = min(min_distance, dist_1[i][j] + dist_2[i][j])

    return min_distance if min_distance != float('inf') else -1

def process_map(n, m, grid):
    # List of numbered houses
    start_positions_1 = []
    start_positions_2 = []
    start_positions_3 = []

    for i in range(n):
        for j in range(m):
            if grid[i][j] == '1':
                start_positions_1.append((i, j))
            elif grid[i][j] == '2':
                start_positions_2.append((i, j))
            elif grid[i][j] == '3':
                start_positions_3.append((i, j))

    # Calculating the minimum distances between groups
    dist_1_2 = min_distance_between_groups(start_positions_1, start_positions_2, n, m, grid) - 1
    dist_2_3 = min_distance_between_groups(start_positions_2, start_positions_3, n, m, grid) - 1
    dist_1_3 = min_distance_between_groups(start_positions_1, start_positions_3, n, m, grid) - 1

    # Constructing edges for the minimum spanning tree
    edges = []
    if dist_1_2 != -1:
        edges.append((dist_1_2, 0, 1))  # Edge between territory 1 and 2
    if dist_2_3 != -1:
        edges.append((dist_2_3, 1, 2))  # Edge between territory 2 and 3
    if dist_1_3 != -1:
        edges.append((dist_1_3, 0, 2))  # Edge between territory 1 and 3

    # Performing Kruskal's algorithm for minimum spanning tree
    return min_spanning_tree(edges, 3)

def min_spanning_tree(edges, num_nodes):
    # Kruskal's algorithm for finding the minimum spanning tree
    edges.sort()  # Sorting edges by weight
    parent = list(range(num_nodes))  # Each node is its own parent initially

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        rootX = find(x)
        rootY = find(y)
        if rootX != rootY:
            parent[rootX] = rootY
            return True
        return False

    mst_weight = 0
    mst_edges = 0

    for weight, u, v in edges:
        if union(u, v):
            mst_weight += weight
            mst_edges += 1
            if mst_edges == num_nodes - 1:
                break

    return mst_weight if mst_edges == num_nodes - 1 else -1

# Input
n, m = map(int, input().split())
grid = [input().strip() for _ in range(n)]  # Read grid as whole lines, each line as a string

# Process the map
result = process_map(n, m, grid)

# Output the result
print(result)
