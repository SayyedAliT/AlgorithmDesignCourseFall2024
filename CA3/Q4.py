from collections import defaultdict, deque

def min_wood_planks(n, heights, edges):
    # Build the tree as an adjacency list
    tree = defaultdict(list)
    for u, v in edges:
        tree[u].append(v)
        tree[v].append(u)

    # Initialize variables
    required_heights = [0] * (n + 1)  # To store the required heights at each node
    visited = [False] * (n + 1)
    total_planks = 0

    # Perform a DFS to calculate the required heights
    def dfs(node):
        nonlocal total_planks
        visited[node] = True
        max_height = heights[node - 1]  # The minimum required height is the given height

        for neighbor in tree[node]:
            if not visited[neighbor]:
                child_height = dfs(neighbor)
                max_height = max(max_height, child_height)  # Ensure the height condition

        # Calculate the additional planks needed
        if max_height > required_heights[node]:
            total_planks += max_height - required_heights[node]
            required_heights[node] = max_height

        return required_heights[node]

    # Start DFS from node 1 (assuming the root is node 1)
    dfs(1)

    return total_planks

# Input processing
if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().splitlines()

    # Number of observation points
    n = int(data[0])

    # Heights of the observation points
    heights = list(map(int, data[1].split()))

    # Edges of the tree
    edges = [tuple(map(int, line.split())) for line in data[2:]]

    # Calculate the result
    result = min_wood_planks(n, heights, edges)

    # Print the output
    print(result)
