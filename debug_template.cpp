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

using namespace std;

#define DEBUG_ON 0

#if DEBUG_ON
#include<sstream>

void printVec() {
    for (auto p : ???)
        cout << ...  << " " << ... << endl;
}
#endif

...

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
    ifstream fin("???.in");
#endif
    return 0;
}
