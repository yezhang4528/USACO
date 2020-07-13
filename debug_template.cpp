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

void printVec(vector<routeInfo>& v) {
    for (int i = 1; i <= MAX_CITY; i++)
        if (v[i].cost != 0)
            cout << i << ": " << v[i].cost  << " " << v[i].legs << endl;
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
        inputFile = "xxx.in";

    ifstream fin(inputFile);

    ...
    return 0;
}
