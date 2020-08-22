#include<iostream>
#include<fstream>
#include<vector>
#include<queue>
#include<climits>

using namespace std;

typedef pair<int, int> pi;

int dijkstra(vector<vector<pi>>& gps, vector<int>& dist, int start, int N) {
    priority_queue<pi, vector<pi>, greater<pi>> q;
    dist[start] = 0;
    q.push(make_pair(dist[start], start));
    while (!q.empty()) {
        int u = q.top().second;
        q.pop();
        for (int i = 0; i < gps[u].size(); ++i) {
            int nxt = gps[u][i].second;
            if (dist[u] + gps[u][i].first < dist[nxt]) {
                dist[nxt] = dist[u] + gps[u][i].first;
                q.push(make_pair(dist[nxt], nxt));
            }
        }
    }
    return dist[N];
}

int main() {

    ifstream fin("gpsduel.in");
    int N, M;
    fin >> N >> M;

    vector<vector<pi>> gps1(N+1);
    vector<vector<pi>> gps2(N+1);
    for (int i = 0; i < M; ++i) {
        int n1, n2, glen1, glen2;
        fin >> n1 >> n2 >> glen1 >> glen2;
        gps1[n2].push_back(make_pair(glen1, n1));
        gps2[n2].push_back(make_pair(glen2, n1));
    }

    vector<int> dist1(N+1, INT_MAX);
    vector<int> dist2(N+1, INT_MAX);
    dijkstra(gps1, dist1, N, N);
    dijkstra(gps2, dist2, N, N);

    // Build complain path.
    vector<vector<pi>> cPath(N+1);
    for (int i = 1; i <= N; ++i) {
        for (int j = 0; j < gps1[i].size(); ++j) {
            int complain = 0;
            int n = gps1[i][j].second;
            int edge1 = gps1[i][j].first, edge2 = gps2[i][j].first;
            if (dist1[n] - dist1[i] != edge1) ++complain;
            if (dist2[n] - dist2[i] != edge2) ++complain;
            cPath[n].push_back(make_pair(complain, i));
        }
    }
    vector<int> dist3(N+1, INT_MAX);
    int leastComplain = dijkstra(cPath, dist3, 1, N);

    ofstream fout("gpsduel.out");
    fout << leastComplain << endl;
    return 0;
}
