/*
 * To run debug version. Set DEBUG_ON to 1
 * #define DEBUG_ON 1
 *
 * The debug program will read input file under ./data/, to read #.in,
 * $ ./a.out 1
 * $ ./a.out 2
 *
 * Compare xxx.out with data/#.out.
 */
#include<iostream>
#include<fstream>
#include<vector>
#include<queue>
#include<algorithm>
#include<climits>
#include<sstream>

using namespace std;
#define DEBUG_ON 0

const int TOTAL_PATH = 3;
typedef pair<int, int> pi;
vector<vector<pi>> gps1;              // first: node index, second: length
vector<vector<pi>> gps2;
vector<vector<pi>> v;
vector<vector<int>> dists(TOTAL_PATH);   // 0: GPS1 route, 1: GPS2 route, 2: shortest route


int dijkstra(vector<vector<pair<int, int>>>& gps, vector<int>& dist, int start) {
    priority_queue<pi, vector<pi>, greater<pi>> q; // Min priority queue ordered by first element, minDist

    dist[start] = 0;    // Farmer John want to start from 1, goes to intersection N.
    q.push(make_pair(0, start));
    while (!q.empty()) {
        int cur = q.top().second;
        q.pop();
        for (int j = 0; j < gps[cur].size(); ++j) {
            int nxt = gps[cur][j].first;
            int newUnits = dist[cur] + gps[cur][j].second;
            if (newUnits < dist[nxt]) {
                dist[nxt] = newUnits;
                q.push(make_pair(newUnits, nxt));
            }
        }
    }
    return dist[gps.size() - 1];
}

int main(int argc, char *argv[])
{
    string inputFile = "";
#if DEBUG_ON

    if (argc > 1) {
        ostringstream os;
        os << "./data/" << argv[1] << ".in";
        ifstream fin(os.str());
        inputFile = os.str();
    }
#endif

    if (inputFile.size() == 0)
        inputFile = "gpsduel.in";

    ifstream fin(inputFile);
    int N, M;
    fin >> N >> M;

    gps1.resize(N+1);
    gps2.resize(N+1);
    v.resize(N+1);
    for (int i = 1; i <= M; ++i) {
        int ai, bi, p, q;
        fin >> ai >> bi >> p >> q;
        // To calculate shortest distance from i to N, we need to reverse travel from N to i,
        // otherwise we can only get the shortest distance from starting point to N.
        gps1[bi].push_back(make_pair(ai, p));
        gps2[bi].push_back(make_pair(ai, q));
    }

    for (int i = 0; i < TOTAL_PATH; ++i)
        dists[i].resize(N+1, INT_MAX);

    dijkstra(gps1, dists[0], N);    // Calculate GPS1 shortest path with dijkstra algo
    dijkstra(gps2, dists[1], N);    // Calculate GPS2 shortest path with dijkstra algo

    /* Generate complain graph
     * Start from 1, go through each path, compare path with shortest dist[], if same, no complain,
     * Otherwise, the gps complains, add 1 to cnt, 
     */
    for (int from = 1; from <= N; ++from) {
        for (int j = 0; j < gps1[from].size(); ++j) {
            int nxt = gps1[from][j].first;
            int cnt = 0;
            int u1 = gps1[from][j].second, u2 = gps2[from][j].second;
            if (dists[0][nxt] - dists[0][from] != u1) ++cnt;
            if (dists[1][nxt] - dists[1][from] != u2) ++cnt;
            v[nxt].push_back(make_pair(from, cnt));
            
        }
    }
    int ans = dijkstra(v, dists[2], 1);
    ofstream fout("gpsduel.out");
    fout << ans << endl;

    return 0;
}
