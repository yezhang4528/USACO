#include<iostream>
#include<fstream>
#include<vector>
#include<climits>
#include<queue>

using namespace std;

#define MAX_N 250

typedef pair<int, int> pi;
vector<vector<int>> edges(MAX_N+1, vector<int>(MAX_N+1, 0));
vector<int> shortestPath;

int dijkstra(int N) {
    int len = 0;
    vector<int> dist(MAX_N+1, INT_MAX);
    priority_queue<pi, vector<pi>, greater<pi>> q;
    dist[1] = 0;
    q.push(make_pair(0, 1));
    while (!q.empty()) {
        int cur = q.top().second;
        int curL = q.top().first;
        cout << "Node: " << cur << ", len " << curL << endl;
        q.pop();
        len += curL;
        shortestPath.push_back(cur);
        if (cur == N)
            break;
        for (int i = 2; i <= N; ++i) {
            int edgeLen = edges[cur][i];
            if (edgeLen && (dist[i] == INT_MAX || dist[i] > dist[cur] + edgeLen)) {
                dist[i] = dist[cur] + edgeLen;
                q.push(make_pair(edgeLen, i));
            }
        }
    }
    return len;
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
    cout << shortestLen << endl;


    return 0;
}
