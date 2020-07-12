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

void printVec(vector<double>& v) {
    for (int i = 0; i < v.size(); i++) {
        cout << i << ": " << v[i] << endl;
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
        inputFile = "homework.in";

    int N;
    ifstream fin(inputFile);

    fin >> N;
    vector<int> homeworks(N+1);
    for (int i = 1; i <= N; ++i) {
        fin >> homeworks[i];
    }

    vector<double> scores(N+1);
    vector<int> loc;
    scores[N-1] = max(homeworks[N], homeworks[N-1]);
    double minimum = min(homeworks[N], homeworks[N-1]);
    double maximum = scores[N-1];
    loc.push_back(N-2);
    int count = 1;
    for (int i = N-2; i > 1; --i) {
        if (homeworks[i] < minimum) {
            scores[i] = (scores[i+1]*count + minimum) / (count+1);
            minimum = homeworks[i];
        } else {
            scores[i] = (scores[i+1]*count + homeworks[i]) / (count+1);
        }
        if (scores[i] > maximum) {
            loc.clear();
            loc.push_back(i-1);
            maximum = scores[i];
        } else if (scores[i] == maximum) {
            loc.insert(loc.begin(), i-1);
        }
        count++;
    }
    //printVec(scores);

    ofstream fout("homework.out");
    for (int i = 0; i < loc.size(); ++i)
        fout << loc[i] << endl;

    return 0;
}
