#include<iostream>
#include<fstream>
#include<vector>
#include<climits>

using namespace std;

#define MAX_FLIGHTS 1000

struct routeInfo {
    long long cost;
    int legs;
    routeInfo(long long x, int y) : cost(x), legs(y) {}
};

vector<vector<routeInfo>> routes(MAX_FLIGHTS + 1, vector<routeInfo>(MAX_FLIGHTS+1, {0, 0}));

void fillRoutes(vector<int>& cities, long long c) {
    for (int i = 1; i < cities.size(); ++i) {
        int to = cities[i];
        for (int j = 0; j < i; ++j) {
            int from = cities[j];
            if (routes[from][to].cost == 0 || routes[from][to].cost > c) {
                routes[from][to].cost = c;
                routes[from][to].legs = i - j;
            }
        }
    }
}

int minDistance(vector<long long>& dist, vector<bool>& visited) {
    long long minDist = LLONG_MAX;
    int minIndex = -1;
    for (int i = 1; i <= MAX_FLIGHTS; ++i) {
        if (visited[i])
            continue;
        if (minIndex == -1 || dist[i] < minDist) {
            minDist = dist[i];
            minIndex = i;
        }
    }
    return minIndex;
}

routeInfo dijkstra(int src, int dst) {
    vector<long long> dist(MAX_FLIGHTS+1, LLONG_MAX);
    vector<int> legs(MAX_FLIGHTS+1, 0);
    vector<bool> visited(MAX_FLIGHTS+1);

    dist[src] = 0;
    for (int i = 1; i <= MAX_FLIGHTS; ++i) {
        int u = minDistance(dist, visited);
        visited[u] = true;
        for (int j = 1; j <= MAX_FLIGHTS; ++j) {
            long long c = routes[u][j].cost;
            if (!visited[j] && c && dist[u] != LLONG_MAX && dist[u] + c <= dist[j]) {
                if (legs[j] == 0 || dist[u] + c < dist[j])
                    legs[j] = legs[u] + routes[u][j].legs;
                else
                    legs[j] = min(legs[u] + routes[u][j].legs, legs[j]);
                dist[j] = dist[u] + c;
            }
        }
    }

    return {dist[dst], legs[dst]};

}

int main() {
    ifstream fin("cowroute.in");

    int A, B, N;
    fin >> A >> B >> N;

    for (int i = 0; i < N; ++i) {
        long long c;
        int n;
        fin >> c >> n;
        vector<int> cities(n);
        for (int j = 0; j < n; ++j)
            fin >> cities[j];
        fillRoutes(cities, c);
    }

    routeInfo ret = dijkstra(A, B);

    ofstream fout("cowroute.out");
    if (ret.cost == LLONG_MAX) {
        fout << -1 << " " << -1 << endl;
    } else {
        fout << ret.cost << " " << ret.legs << endl;
    }

    return 0;
}
