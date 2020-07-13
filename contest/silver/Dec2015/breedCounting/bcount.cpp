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

#define DEBUG_ON 0

#if DEBUG_ON
#include<sstream>

void printMatrix(vector<vector<int>>& v) {
    for (auto r : v) {
        for (auto c : r)
            cout << c << " ";
        cout << endl;
    }
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
        inputFile = "bcount.in";

    ifstream fin(inputFile);

    const int MAX_BREEDID = 3;
    int N, Q;
    fin >> N >> Q;

    vector<vector<int>> counts(MAX_BREEDID+1, vector<int>(N+1, 0));
    for (int i = 1; i <= N; ++i) {
        int breedId;
        fin >> breedId;
        counts[breedId][i]++;
        for (int j = 1; j <= 3; ++j) {
            counts[j][i] += counts[j][i-1];
        }
    }

    ofstream fout("bcount.out");
    for (int i = 0; i < Q; ++i) {
        int start, end;
        fin >> start >> end;
        fout << counts[1][end] - counts[1][start-1] << " "
             << counts[2][end] - counts[2][start-1] << " "
             << counts[3][end] - counts[3][start-1] << endl;
    }
    return 0;
}
