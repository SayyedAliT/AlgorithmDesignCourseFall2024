#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
#include <climits>
#include <cstring>

using namespace std;

struct Edge {
    int to, capacity, flow;
    Edge* rev; // Pointer to the reverse edge
    Edge(int to, int capacity) : to(to), capacity(capacity), flow(0), rev(nullptr) {}
};

struct Node {
    vector<Edge*> edges;
    bool is_full = true;
};

void add_edge(Node& u, Node& v, int capacity) {
    Edge* forward = new Edge(&v - &u, capacity);
    Edge* backward = new Edge(&u - &v, 0); // Reverse edge with 0 capacity
    forward->rev = backward;
    backward->rev = forward;
    u.edges.push_back(forward);
    v.edges.push_back(backward);
}

void read_input(int& n, vector<string>& grid) {
    cin >> n;
    grid.resize(2 * n - 1);
    for (int i = 0; i < 2 * n - 1; ++i) {
        cin >> grid[i];
    }
}

void create_nodes(int n, const vector<string>& grid, vector<Node>& nodes, Node& source, Node& sink) {
    nodes.resize(n * n);
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            bool is_left = (i + j) % 2 == 0;
            int i_grid = 2 * (i + 1) - 1;
            int j_grid = 2 * (j + 1) - 1;
            int count = 0;

            for (auto [di, dj] : vector<pair<int, int>>{{-1, 0}, {1, 0}, {0, -1}, {0, 1}}) {
                int ni = i_grid + di, nj = j_grid + dj;
                if (grid[ni][nj] == '|' || grid[ni][nj] == '-') continue;
                count++;
            }

            if (count - 1 > 0) {
                nodes[i * n + j].is_full = false;
                if (is_left) {
                    add_edge(source, nodes[i * n + j], count - 1);
                } else {
                    add_edge(nodes[i * n + j], sink, count - 1);
                }
            }
        }
    }
}

bool bfs_build_level_graph(const vector<Node>& nodes, Node& source, Node& sink, vector<int>& level) {
    fill(level.begin(), level.end(), -1);
    queue<int> q;
    q.push(&source - &nodes[0]);
    level[&source - &nodes[0]] = 0;

    while (!q.empty()) {
        int u = q.front();
        q.pop();

        for (auto e : nodes[u].edges) {
            if (level[e->to] == -1 && e->flow < e->capacity) {
                level[e->to] = level[u] + 1;
                q.push(e->to);
            }
        }
    }

    return level[&sink - &nodes[0]] != -1;
}

int send_flow_dfs(int u, int flow, Node& sink, const vector<int>& level, vector<int>& start, vector<Node>& nodes) {
    if (u == &sink - &nodes[0]) return flow;

    for (; start[u] < nodes[u].edges.size(); ++start[u]) {
        Edge* e = nodes[u].edges[start[u]];

        if (level[e->to] == level[u] + 1 && e->flow < e->capacity) {
            int curr_flow = min(flow, e->capacity - e->flow);
            int temp_flow = send_flow_dfs(e->to, curr_flow, sink, level, start, nodes);

            if (temp_flow > 0) {
                e->flow += temp_flow;
                e->rev->flow -= temp_flow;
                return temp_flow;
            }
        }
    }

    return 0;
}

int dinic_max_flow(vector<Node>& nodes, Node& source, Node& sink) {
    int max_flow = 0;
    vector<int> level(nodes.size());
    vector<int> start(nodes.size());

    while (bfs_build_level_graph(nodes, source, sink, level)) {
        fill(start.begin(), start.end(), 0);

        while (int flow = send_flow_dfs(&source - &nodes[0], INT_MAX, sink, level, start, nodes)) {
            max_flow += flow;
        }
    }

    return max_flow;
}

int main() {
    int n;
    vector<string> grid;
    read_input(n, grid);

    vector<Node> nodes;
    Node source, sink;

    create_nodes(n - 1, grid, nodes, source, sink);
    cout << dinic_max_flow(nodes, source, sink) << endl;

    return 0;
}
