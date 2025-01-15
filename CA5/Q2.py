class Graph:
    def __init__(self):
        self.nodes = []
        self.edges = []
        self.capacity = {}
        self.flow = {}
        self.parent = {}

    def add_node(self, name):
        node = Node(name)
        self.nodes.append(node)
        return node

    def add_edge(self, from_node, to_node):
        edge = (from_node, to_node)
        self.edges.append(edge)
        self.capacity[edge] = 1
        self.flow[edge] = 0
        self.flow[(to_node, from_node)] = 0
        from_node.add_outcome_edge(edge)
        to_node.add_income_edge(edge)

    def ford_fulkerson(self, source, sink):
        while True:
            self._reset_flow()
            self._dfs(source, float('inf'))

            if self.flow[sink] is None:
                return self.flow

            self._update_flow(source, sink)

    def _reset_flow(self):
        for node in self.nodes:
            self.flow[node] = None

    def _dfs(self, node, flow_value):
        self.flow[node] = flow_value
        for edge in node.outcome_edges:
            _, to_node = edge
            if self.flow[to_node] is None and self.capacity[edge] - self.flow[edge] > 0:
                self.parent[to_node] = node
                self._dfs(to_node, min(flow_value, self.capacity[edge] - self.flow[edge]))

        for edge in node.income_edges:
            from_node, _ = edge
            if self.flow[from_node] is None and self.flow[edge] > 0:
                self.parent[from_node] = node
                self._dfs(from_node, min(flow_value, self.flow[edge]))

    def _update_flow(self, source, sink):
        current_node = sink
        flow_value = self.flow[sink]
        while current_node != source:
            parent_node = self.parent[current_node]
            edge = (parent_node, current_node)
            reverse_edge = (current_node, parent_node)
            self.flow[edge] += flow_value
            self.flow[reverse_edge] -= flow_value
            current_node = parent_node

    def get_max_flow(self, source):
        return sum(self.flow[edge] for edge in source.outcome_edges)

    def get_path_with_cost(self, start, end):
        path = []
        current = start
        while current != end:
            path.append(current)
            found = False
            for edge in current.outcome_edges:
                if self.flow[edge] > 0:
                    self.flow[edge] -= 1
                    current = edge[1]
                    found = True
                    break
            if not found:
                break
        if current == end:
            path.append(end)
        return path if path[-1] == end else []


class Node:
    def __init__(self, name):
        self.name = name
        self.income_edges = []
        self.outcome_edges = []

    def add_income_edge(self, edge):
        self.income_edges.append(edge)

    def add_outcome_edge(self, edge):
        self.outcome_edges.append(edge)


class MaxFlowSolver:
    def __init__(self):
        self.graph = Graph()

    def read_input(self):
        n, m = map(int, input().split())
        for i in range(n):
            self.graph.add_node(i)

        for _ in range(m):
            a, b = map(int, input().split())
            self.graph.add_edge(self.graph.nodes[a - 1], self.graph.nodes[b - 1])

        def solve(self):
            source = self.graph.nodes[0]
            sink = self.graph.nodes[-1]
            self.graph.ford_fulkerson(source, sink)
            max_flow = self.graph.get_max_flow(source)
            print(max_flow)

            self.print_all_paths(source, sink, max_flow)

        def print_all_paths(self, source, sink, max_flow):
            for _ in range(max_flow):
                path = self.graph.get_path_with_cost(source, sink)
                self.print_path(path)

        def print_path(self, path):
            print(len(path))
            path_str = ' '.join(str(node.name + 1) for node in path)
            print(path_str)

    def main():
        solver = MaxFlowSolver()
        solver.read_input()
        solver.solve()

    if __name__ == "__main__":
        main()