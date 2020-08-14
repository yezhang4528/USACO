#include<iostream>
#include<fstream>
#include<vector>
#include<climits>
#include<queue>

using namespace std;

#define MAX_N 250

typedef pair<int, int> pi;
vector<vector<int>> edges(MAX_N+1, vector<int>(MAX_N+1, 0));
vector<int> shortestPath(MAX_N+1);  // Each pos/index contains prev pos/index of the shortest path

#if 0
void printShortestPath(int N) {
    int n = N;
    cout << N;
    while (n >= 1) {
        if (shortestPath[n]) {
            cout << "<=" << shortestPath[n];
            n = shortestPath[n];
        } else {
            --n;
        }
    }
    cout << endl;
}
void printVec(int N) {
    for (int i = 0; i <= N; ++i) {
        cout << shortestPath[i] << " ";
    }
    cout << endl;
}
#endif

int dijkstra(int N) {
    vector<int> dist(MAX_N+1, INT_MAX);
    priority_queue<pi, vector<pi>, greater<pi>> q;
    vector<bool> visited(MAX_N+1);

    dist[1] = 0;
    q.push(make_pair(0, 1));
    while (!q.empty()) {
        int cur = q.top().second;
        int curL = q.top().first;
        q.pop();
        for (int i = 2; i <= N; ++i) {
            if (visited[i])
                continue;

            int edgeLen = edges[cur][i];
            if (edgeLen && dist[i] > dist[cur] + edgeLen) {
                dist[i] = dist[cur] + edgeLen;
                shortestPath[i] = cur;
                q.push(make_pair(edgeLen, i));
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
        int A, B, L;
        fin >> A >> B >> L;
        edges[A][B] = L;
        edges[B][A] = L;
    }

    int shortestLen = dijkstra(N);
    //cout << shortestLen << endl;
    //printShortestPath(N);
    //printVec(N);

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
