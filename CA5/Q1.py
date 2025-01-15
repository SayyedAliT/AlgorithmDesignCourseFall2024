from collections import deque


class FlowSolver:
    class Vertex:
        def __init__(self):
            self.adjacency = []
            self.full = True

    class Arc:
        def __init__(self, destination, capacity):
            self.destination = destination
            self.capacity = capacity
            self.flow = 0
            self.reverse = None

    def __init__(self):
        self.vertices = []
        self.start = self.Vertex()
        self.end = self.Vertex()

    def add_connection(self, start, destination, capacity):
        forward = self.Arc(destination, capacity)
        backward = self.Arc(start, 0)
        forward.reverse = backward
        backward.reverse = forward
        self._connect_vertices(start, destination, forward, backward)

    def _connect_vertices(self, start, destination, forward, backward):
        start.adjacency.append(forward)
        destination.adjacency.append(backward)

    def input_grid(self):
        n = int(input().strip())
        grid = self._load_grid(n)
        return n, grid

    def _load_grid(self, n):
        grid = [list(input().strip()) for _ in range(2 * n - 1)]
        return grid

    def initialize_vertices(self, n, grid):
        i = 0
        while i < n:
            j = 0
            while j < n:
                vertex = self.Vertex()
                self._configure_vertex(i, j, grid, vertex)
                self.vertices.append(vertex)
                j = j + 1
            i = i + 1

        self._create_edges_for_non_full_vertices(n, grid)
    def _configure_vertex(self, i, j, grid, vertex):
        left_side = False
        if (i + j) % 2 == 0:
            left_side = True
        row = 2 * (i + 1) - 1
        col = 2 * (j + 1) - 1

        adjacent_count = self._check_adjacent_cells(row, col, grid)

        if adjacent_count - 1 > 0:
            vertex.full = False
            self._connect_based_on_side(left_side, vertex, adjacent_count - 1)

    def _check_adjacent_cells(self, row, col, grid):
        count = 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dx, dy in directions:
            new_row = row + dx
            new_col = col + dy
            cell_value = grid[new_row][new_col]
            if cell_value != '|':
                if cell_value != '-':
                    count = count + 1
        return count

    def _connect_based_on_side(self, left_side, vertex, capacity):
        if left_side:
            self.add_connection(self.start, vertex, capacity)
        else:
            self.add_connection(vertex, self.end, capacity)

    def _create_edges_for_non_full_vertices(self, n, grid):
        i = 0
        while i < n:
            j = 0
            while j < n:
                idx = i * n + j
                if not self.vertices[idx].full:
                    left_side = False
                    sum_ij = i + j
                    if sum_ij % 2 == 0:
                        left_side = True
                    row = 2 * (i + 1) - 1
                    col = 2 * (j + 1) - 1

                    adjacent_out_of_bounds = self._link_adjacent_vertices(i, j, n, grid, idx, left_side, row, col)
                    self._add_edges_for_out_of_bounds(idx, left_side, adjacent_out_of_bounds)
                j = j + 1
            i = i + 1
    def _link_adjacent_vertices(self, i, j, n, grid, idx, left_side, row, col):
        adjacent_out_of_bounds = 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        direction_index = 0
        while direction_index < len(directions):
            dx, dy = directions[direction_index]
            if grid[row + dx][col + dy] != '|':
                if grid[row + dx][col + dy] != '-':
                    ni = i + dx
                    nj = j + dy
                    if 0 <= ni:
                        if ni < n:
                            if 0 <= nj:
                                if nj < n:
                                    if left_side:
                                        if not self.vertices[ni * n + nj].full:
                                            self.add_connection(self.vertices[idx], self.vertices[ni * n + nj], 1)
                                else:
                                    adjacent_out_of_bounds = adjacent_out_of_bounds + 1
                            else:
                                adjacent_out_of_bounds = adjacent_out_of_bounds + 1
                        else:
                            adjacent_out_of_bounds = adjacent_out_of_bounds + 1
                    else:
                        adjacent_out_of_bounds = adjacent_out_of_bounds + 1
            direction_index = direction_index + 1
        return adjacent_out_of_bounds
    def _add_edges_for_out_of_bounds(self, idx, left_side, adjacent_out_of_bounds):
        if adjacent_out_of_bounds > 0:
            if left_side:
                self.add_connection(self.vertices[idx], self.end, adjacent_out_of_bounds)
            else:
                self.add_connection(self.start, self.vertices[idx], adjacent_out_of_bounds)

    def breadth_first_search(self, levels):
        for vertex in self.vertices:
            levels[vertex] = -1
        queue = deque([self.start])
        levels[self.start] = 0
        self._perform_bfs(levels, queue)
        return levels[self.end] != -1

    def _perform_bfs(self, levels, queue):
        while queue:
            u = queue.popleft()
            for arc in u.adjacency:
                if levels[arc.destination] < 0:
                    if arc.flow < arc.capacity:
                        levels[arc.destination] = levels[u] + 1
                        queue.append(arc.destination)

    def depth_first_search(self, u, flow, levels, start_indices):
        if u == self.end:
            return flow

        while start_indices[u] < len(u.adjacency):
            arc = u.adjacency[start_indices[u]]
            if levels[arc.destination] == levels[u] + 1:
                if arc.flow < arc.capacity:
                    available_flow = arc.capacity - arc.flow
                    min_flow = min(flow, available_flow)

                    flow_sent = self._send_flow(arc, min_flow, levels, start_indices)
                    if flow_sent > 0:
                        return flow_sent
            start_indices[u] = start_indices[u] + 1
        return 0

    def _send_flow(self, arc, min_flow, levels, start_indices):
        flow_sent = self.depth_first_search(arc.destination, min_flow, levels, start_indices)
        if flow_sent > 0:
            arc.flow = arc.flow + flow_sent
            arc.reverse.flow = arc.reverse.flow - flow_sent
        return flow_sent

    def max_flow_algorithm(self):
        total_flow = 0
        levels = {}

        while self.breadth_first_search(levels):
            start_indices = {vertex: 0 for vertex in self.vertices}
            while True:
                flow_sent = self.depth_first_search(self.start, float('inf'), levels, start_indices)
                if flow_sent <= 0:
                    break
                total_flow = total_flow + flow_sent

        return total_flow

    def solve_problem(self, n, grid):
        self.initialize_vertices(n - 1, grid)
        self.vertices.append(self.start)
        self.vertices.append(self.end)
        return self.max_flow_algorithm()


if __name__ == '__main__':
    solver = FlowSolver()
    n, grid = solver.input_grid()
    result = solver.solve_problem(n, grid)
    print(result)
