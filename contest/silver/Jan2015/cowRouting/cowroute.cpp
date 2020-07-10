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
#include<climits>
#include<algorithm>

using namespace std;

#define DEBUG_ON 0

#define MAX_CITY 1000

struct routeInfo {
    long long cost;
    int legs;
    routeInfo(long long c, int l) : cost(c), legs(l) {}
};

#if DEBUG_ON
#include<sstream>

void printVec(vector<routeInfo>& v) {
    for (int i = 1; i <= MAX_CITY; i++)
        if (v[i].cost != 0)
            cout << i << ": " << v[i].cost  << " " << v[i].legs << endl;
}
#endif

vector<vector<routeInfo>> rtList(MAX_CITY+1, vector<routeInfo>(MAX_CITY+1, {0, 0}));

void fillRtList(long long cost, vector<int>& cities) {
    for (int i = 0; i < cities.size(); i++) {
        for (int j = 0; j < i; j++) {
            if (rtList[cities[j]][cities[i]].cost == 0 || rtList[cities[j]][cities[i]].cost > cost) {
                rtList[cities[j]][cities[i]].cost = cost;       // From city[j] to city[i] cost
                rtList[cities[j]][cities[i]].legs = i - j;      // Stops along the route
            }
        }
    }

}

int minDistance(vector<bool>& sptSet, vector<long long>& dist) {
    int minIndex = -1;
    for (int i = 1; i <= MAX_CITY; i++) {
        if (sptSet[i])
            continue;
        if (minIndex == -1 || dist[i] < dist[minIndex]) {
            minIndex = i;
        }
    }
    return minIndex;
}

routeInfo dijsktraCalCost(int s, int d) {
    vector<bool> visited(MAX_CITY+1);
    vector<long long> dist(MAX_CITY+1, LLONG_MAX);
    vector<int> legs(MAX_CITY+1, 0);

    dist[s] = 0;
    for (int c = 1; c <= MAX_CITY; c++) {
        int u = minDistance(visited, dist);
        visited[u] = true;
        for (int v = 1; v <= MAX_CITY; v++) {
            long long newCost = dist[u] + rtList[u][v].cost;
            if (!visited[v] && rtList[u][v].cost && dist[u] != LLONG_MAX &&
                newCost <= dist[v]) {
                if (newCost < dist[v] || legs[v] == 0)  // update legs
                    legs[v] = legs[u] + rtList[u][v].legs;
                else
                    legs[v] = min(legs[u] + rtList[u][v].legs, legs[v]);
                dist[v] = dist[u] + rtList[u][v].cost;
            }
        }
    }

    return {dist[d], legs[d]};
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
        inputFile = "cowroute.in";

    ifstream fin(inputFile);

    int A, B, N;
    fin >> A >> B >> N;

    for (int i = 0; i < N; i++) {
        long long c;
        int cityNum;
        fin >> c >> cityNum;
        vector<int> cities(cityNum);
        for (int j = 0; j < cityNum; j++)
            fin >> cities[j];
        fillRtList(c, cities);
    }
    //printVec(rtList[270]);
    routeInfo ret = dijsktraCalCost(A, B);

    ofstream fout("cowroute.out");
    if (ret.cost == LLONG_MAX && ret.legs == 0)
        fout << -1 << " " << -1 << endl;
    else
        fout << ret.cost << " " << ret.legs << endl;
    return 0;
}
