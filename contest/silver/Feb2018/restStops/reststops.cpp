#include<iostream>
#include<fstream>
#include<algorithm>
#include<vector>

using namespace std;

#define DEBUG_ON 0

int L, N, rf, rb;
vector<pair<int, int>> stops;

#if DEBUG_ON
#include<sstream>

void printVec() {
    for (auto p : stops)
        cout << p.first << " " << p.second << endl;
}
#endif

long long calMaxTasty() {
    long long tasty = 0;
    int finished = 0;

    for (int i = stops.size() - 1; i >= 0; i--) {
        if (stops[i].second <= finished)
            continue;

        tasty += (long long)(stops[i].second - finished) * (rf - rb) * stops[i].first;
        finished = stops[i].second;
    }

    return tasty;
}

int main(int argc, char *argv[])
{
#if DEBUG_ON
    if (argc <= 1) {
        cout << argv[0] << " takes one integer argument" << endl;
        return 0;
    }
    ostringstream os;
    os << "./data/" << argv[1] << ".in";
    ifstream fin(os.str());
    
#else
    ifstream fin("reststops.in");
#endif
    fin >> L >> N >> rf >> rb;

    stops.resize(N);
    for (int i = 0; i < N; i++)
        fin >> stops[i].second >> stops[i].first;    // First: tasty. Second: distance

    sort(stops.begin(), stops.end());
#if DEBUG_ON
    printVec();
#endif

    long long maxUnits = calMaxTasty();
    ofstream fout("reststops.out");
    fout << maxUnits << endl;
    return 0;
}
