#include <iostream>
#include <vector>
#include <queue>
#include <string>
#include <algorithm>
#include <limits>
#include <tuple>

using namespace std;

const int INF = numeric_limits<int>::max();
const vector<pair<int, int>> directions = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};

// Function to read input
vector<string> readGrid(int n, int m) {
    vector<string> grid(n);
    for (int i = 0; i < n; ++i) {
        cin >> grid[i];
    }
    return grid;
}

// Function to initialize distances
vector<vector<vector<int>>> initializeDistances(int n, int m) {
    return vector<vector<vector<int>>>(n, vector<vector<int>>(m, vector<int>(3, INF)));
}

// Function to check if a cell is valid
bool isValidCell(int x, int y, int n, int m, const vector<string>& grid, const vector<vector<bool>>& visited) {
    return x >= 0 && x < n && y >= 0 && y < m && !visited[x][y] && grid[x][y] != '#';
}

// Function to perform BFS for a specific target
void bfsForTarget(const vector<string>& grid, vector<vector<vector<int>>>& distances, int target) {
    int n = grid.size(), m = grid[0].size();
    vector<vector<bool>> visited(n, vector<bool>(m, false));
    queue<tuple<int, int, int>> q;

    // Add all target cells to the queue
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            if (grid[i][j] == target + '0') {
                q.push(make_tuple(i, j, 0));
                visited[i][j] = true;
            }
        }
    }

    // BFS
    while (!q.empty()) {
        auto [x, y, d] = q.front();
        q.pop();

        distances[x][y][target - 1] = d;

        for (auto [dx, dy] : directions) {
            int nx = x + dx, ny = y + dy;
            if (isValidCell(nx, ny, n, m, grid, visited)) {
                visited[nx][ny] = true;
                q.push(make_tuple(nx, ny, d + 1));
            }
        }
    }
}

// Function to find minimum distance between two types
int minDistanceBetweenTypes(const vector<string>& grid, int type1, int type2) {
    int n = grid.size(), m = grid[0].size();
    vector<vector<bool>> visited(n, vector<bool>(m, false));
    queue<tuple<int, int, int>> q;

    // Add all type1 cells to the queue
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            if (grid[i][j] == type1 + '0') {
                q.push(make_tuple(i, j, 0));
                visited[i][j] = true;
            }
        }
    }

    // BFS to find the nearest type2 cell
    while (!q.empty()) {
        auto [x, y, d] = q.front();
        q.pop();

        if (grid[x][y] == type2 + '0') {
            return d;
        }

        for (auto [dx, dy] : directions) {
            int nx = x + dx, ny = y + dy;
            if (isValidCell(nx, ny, n, m, grid, visited)) {
                visited[nx][ny] = true;
                q.push(make_tuple(nx, ny, d + 1));
            }
        }
    }

    return INF;
}

// Function to calculate distances between types
vector<int> calculateDistancesBetweenTypes(const vector<string>& grid) {
    const vector<pair<int, int>> typePairs = {{1, 2}, {2, 3}, {1, 3}};
    vector<int> distances;

    for (const auto& [type1, type2] : typePairs) {
        int distance = minDistanceBetweenTypes(grid, type1, type2) - 1;
        distances.push_back(distance);
    }

    return distances;
}

// Function to calculate sum of two minimum distances
int sumOfTwoMinDistances(const vector<int>& distances) {
    vector<int> sorted_distances = distances;
    sort(sorted_distances.begin(), sorted_distances.end());
    return sorted_distances[0] + sorted_distances[1];
}

// Function to calculate the final result
int calculateMinDistance(const vector<string>& grid, const vector<vector<vector<int>>>& distances) {
    int n = grid.size(), m = grid[0].size();
    vector<int> distances_between_types = calculateDistancesBetweenTypes(grid);
    int sum_of_two_min = sumOfTwoMinDistances(distances_between_types);

    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            if (grid[i][j] == '.') {
                int sum = distances[i][j][0] + distances[i][j][1] + distances[i][j][2] - 2;
                sum_of_two_min = min(sum_of_two_min, sum);
            }
        }
    }

    return sum_of_two_min;
}

int main() {
    int n, m;
    cin >> n >> m;

    vector<string> grid = readGrid(n, m);
    vector<vector<vector<int>>> distances = initializeDistances(n, m);

    // Perform BFS for each type of cell
    for (int target = 1; target <= 3; ++target) {
        bfsForTarget(grid, distances, target);
    }

    // Calculate and print the result
    int result = calculateMinDistance(grid, distances);
    cout << result << endl;

    return 0;
}
