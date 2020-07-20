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

using namespace std;

struct store {
    int gal;
    int cents;
};

#define DEBUG_ON 0

#if DEBUG_ON
#include<sstream>

void printVec(vector<int>& v) {
    for (auto g : v)
        cout << g << " ";
    cout << endl;
}

void printVecLong(vector<long long>& v) {
    for (auto m : v)
        cout << m << " ";
    cout << endl;
}

void printStores(vector<store>& v) {
    for (auto s : v)
        cout << s.gal << " " << s.cents << endl;
}
#endif

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
        inputFile = "rental.in";

    ifstream fin(inputFile);

    int N, M, R;
    fin >> N >> M >> R;

    vector<int> gallons(N);
    for (int i = 0; i < N; ++i)
        fin >> gallons[i];
    sort(gallons.rbegin(), gallons.rend()); // Sort in decreasing order
    //printVec(gallons);
    
    vector<store> stores(M);
    for (int i = 0; i < M; ++i)
        fin >> stores[i].gal >> stores[i].cents;
    // Sort by cents in struct in decending order.
    sort(stores.begin(), stores.end(), [](const store &left, const store &right) {return left.cents > right.cents;});
    //printStores(stores);

    vector<long long> maxRent(N+1, 0);
    int sidx = 0;       // stores index
    for (int i = 1; i <= N; ++i) {
        maxRent[i] = maxRent[i-1];
        while (sidx < M && gallons[i-1] > 0) {
            int use = min(stores[sidx].gal, gallons[i-1]);
            gallons[i-1] -= use;
            stores[sidx].gal -= use;
            maxRent[i] += (long long)use * stores[sidx].cents;
            if (stores[sidx].gal == 0)
                ++sidx;
        }
    }
    //printVecLong(maxRent);

    vector<int> rents(R);
    for (int i = 0; i < R; ++i)
        fin >> rents[i];
    sort(rents.begin(), rents.end());
    //printVec(rents);

    int ridx = R - 1;
    int j = N;
    long long rentalSoFar = 0;

    while (ridx >= 0 && j >= 1) {
        rentalSoFar += rents[ridx];
        maxRent[j] = max(rentalSoFar + maxRent[j-1], maxRent[j]);
        --ridx;
        --j;
    }

    long long ret = 0;
    for (int i = 1; i <= N; ++i)
        ret = max(ret, maxRent[i]);

    ofstream fout("rental.out");
    fout << ret << endl;

    return 0;
}
