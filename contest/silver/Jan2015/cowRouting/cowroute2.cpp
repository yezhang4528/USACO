#include<iostream>
#include<fstream>
#include<vector>

using namespace std;

#define MAX_CITIES 100

struct routeInfo {
    long long cost;
    int legs;
    routeInfo(long long x, int y) : cost(x), legs(y) {}
};

vector<vector<routeInfo>> routes(MAX_CITIES + 1, vector<routeInfo>(MAX_CITIES+1, {0, 0}));

void fillRoutes(vector<int>& cities, long long c) {
    for (int i = 0; i < cities.size(); ++i) {
        int start = cities[i];
        for (int j = i + 1; j < cities.size(); ++j) {
            int end = cities[j];
            if (routes[start][end].cost == 0 || routes[start][end].cost > c) {
                routes[start][end].cost = c;
                routes[start][end].legs = j - i;
            }
        }
    }
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

    return 0;
}
