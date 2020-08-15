#include<iostream>
#include<fstream>
#include<vector>
#include<climits>

using namespace std;

#define MAX_N 250
vector<vector<int>> edges(MAX_N+1, vector<int>(MAX_N+1, 0));
vector<int> shortestPath(MAX_N+1, 0);

int minDistance(vector<int>& dist, vector<bool>& visited, int N) {
    int minIndex = 0;
    int minDist = INT_MAX;
    for (int i = 1; i <= MAX_N; ++i) {
        if (!visited[i] && dist[i] < minDist) {
            minIndex = i;
            minDist = dist[i];
        }
    }
    return minIndex;
}

int dijkstra(int N) {
    vector<int> dist(MAX_N+1, INT_MAX);
    vector<bool> visited(MAX_N+1);
    dist[1] = 0;
    for (int i = 1; i <= N; ++i) {
        int u = minDistance(dist, visited, N);
        visited[u] = true;
        for (int j = 1; j <= N; ++j) {
            if (!visited[j] && edges[u][j] && (dist[j] == 0 || dist[u] + edges[u][j] < dist[j])) {
                dist[j] = dist[u] + edges[u][j];
                shortestPath[j] = u;
            }
        }
    }
    return dist[N];
}

int main() {
    ifstream fin("rblock.in");

    int N, M;
    fin >> N >> M;

    for (int i = 0; i < M; ++i) {
        int row, col, len;
        fin >> row >> col >> len;
        edges[row][col] = len;
        edges[col][row] = len;
    }

    int shortestLen = dijkstra(N);

    int n = N;
    int maxInc = 0;
    while (n > 1) {
        int prev = shortestPath[n];
        edges[prev][n] <<= 1;
        edges[n][prev] <<= 1;
        int curLen = dijkstra(N);
        maxInc = max(curLen - shortestLen, maxInc);
        edges[prev][n] >>= 1;
        edges[n][prev] >>= 1;
        n = prev;
    }

    ofstream fout("rblock.out");
    fout << maxInc << endl;

    return 0;
}