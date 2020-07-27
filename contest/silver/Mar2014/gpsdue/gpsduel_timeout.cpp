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
#include<algorithm>
#include<climits>

using namespace std;

struct Node {
    int dst;
    int units;
    Node(int a, int b) : dst(a), units(b) {}
};

const int TOTAL_PATH = 3;
vector<vector<Node>> gps1;              // Save shortest distance from i to N for GPS1
vector<vector<Node>> gps2;              // Save shortest distance from i to N for GPS2
vector<vector<Node>> v;
vector<vector<int>> dists(TOTAL_PATH);   // 0: GPS1 route, 1: GPS2 route, 2: shortest route

#define DEBUG_ON 1

#if DEBUG_ON
#include<sstream>

void printVec() {
    for (int i = 1; i < gps1.size(); ++i) {
        cout << i << " => " << endl;;
        for (int j = 0; j < gps1[i].size(); ++j) {
            cout << gps1[i][j].dst << " " << ", g1: " << gps1[i][j].units << ", g2: " << gps2[i][j].units << endl;
        }
        cout << endl;
    }
}

void printDist(vector<int>& dv) {
    for (auto d : dv)
        cout << d << " ";
    cout << endl;
}

#endif

int minDistance(vector<bool>& visited, vector<int>& dist) {
    int minIndex = -1;
    for (int i = 1; i < dist.size(); ++i) {
        if (visited[i])
            continue;
        if (minIndex == -1 || dist[i] < dist[minIndex])
            minIndex = i;
    }
    return minIndex;
}

int dijkstra(vector<vector<Node>>& gps, vector<int>& dist, int start) {
    int N = gps.size() - 1;
    vector<bool> visited(N+1);

    dist[start] = 0;    // Farmer John want to start from 1, goes to intersection N.
    for (int j = 1; j <= N; ++j) {
        int u = minDistance(visited, dist);
        visited[u] = true;
        for (int k = 0; k < gps[u].size(); ++k) {
            int newUnits = dist[u] + gps[u][k].units;
            int newdst = gps[u][k].dst;
            if (!visited[newdst] && newUnits < dist[newdst]) {
                dist[newdst] = newUnits;
            }
        }
    }
    return dist[N];
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
        Node aNew(ai, p), bNew(ai, q);
        // To calculate shortest distance from i to N, we need to reverse travel from N to i,
        // otherwise we can only get the shortest distance from starting point to N.
        gps1[bi].push_back(aNew);
        gps2[bi].push_back(bNew);
    }
    //printVec();

    for (int i = 0; i < TOTAL_PATH; ++i)
        dists[i].resize(N+1, INT_MAX);

    dijkstra(gps1, dists[0], N);    // Calculate GPS1 shortest path with dijkstra algo
    dijkstra(gps2, dists[1], N);    // Calculate GPS2 shortest path with dijkstra algo

    //printDist(dists[0]);
    //printDist(dists[1]);

    /* Generate complain graph
     * Start from 1, go through each path, compare path with shortest dist[], if same, no complain,
     * Otherwise, the gps complains, add 1 to cnt, 
     */
    for (int from = 1; from <= N; ++from) {
        for (int j = 0; j < gps1[from].size(); ++j) {
            int to = gps1[from][j].dst;
            int cnt = 0;
            int u1 = gps1[from][j].units, u2 = gps2[from][j].units;
            if (dists[0][to] - dists[0][from] != u1) ++cnt;
            if (dists[1][to] - dists[1][from] != u2) ++cnt;
            Node d(from, cnt);
            v[to].push_back(d);
            
        }
    }
    int ans = dijkstra(v, dists[2], 1);
    ofstream fout("gpsduel.out");
    fout << ans << endl;

    return 0;
}
