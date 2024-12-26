from collections import deque
from heapq import heappop, heappush


def bfs_to_find_region(grid, start, n, m, region_id, visited):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = deque([start])
    region_cells = []

    while queue:
        x, y = queue.popleft()
        region_cells.append((x, y))

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                if grid[nx][ny] in {'1', '2', '3'} or grid[nx][ny] == '.':
                    visited[nx][ny] = True
                    queue.append((nx, ny))

    return region_cells


def build_distance_matrix(grid, regions, n, m):
    distances = [[float('inf')] * len(regions) for _ in range(len(regions))]

    for i, region_cells in enumerate(regions):
        visited = [[False] * m for _ in range(n)]
        queue = deque([(x, y, 0) for x, y in region_cells])

        while queue:
            x, y, d = queue.popleft()

            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                    visited[nx][ny] = True

                    if grid[nx][ny] in {'1', '2', '3'}:
                        for j, other_region in enumerate(regions):
                            if (nx, ny) in other_region and i != j:
                                distances[i][j] = min(distances[i][j], d)
                                distances[j][i] = distances[i][j]
                    elif grid[nx][ny] == '.':
                        queue.append((nx, ny, d + 1))

    return distances


def min_road_constructions(n, m, grid):
    regions = []
    visited = [[False] * m for _ in range(n)]

    # Find all regions
    for i in range(n):
        for j in range(m):
            if grid[i][j] in {'1', '2', '3'} and not visited[i][j]:
                visited[i][j] = True
                region_cells = bfs_to_find_region(grid, (i, j), n, m, len(regions), visited)
                regions.append(region_cells)

    # If there are fewer than 3 regions, return -1
    if len(regions) < 3:
        return -1

    # Build distance matrix
    distances = build_distance_matrix(grid, regions, n, m)

    # Use Prim's algorithm to find the minimum spanning tree
    pq = [(0, 0)]
    total_cost = 0
    visited_regions = set()

    while pq and len(visited_regions) < len(regions):
        cost, region = heappop(pq)
        if region in visited_regions:
            continue

        visited_regions.add(region)
        total_cost += cost

        for neighbor in range(len(regions)):
            if neighbor not in visited_regions:
                heappush(pq, (distances[region][neighbor], neighbor))

    return total_cost


# Input reading
n, m = map(int, input().split())
grid = [input().strip() for _ in range(n)]

# Solve and output result
print(min_road_constructions(n, m, grid))
