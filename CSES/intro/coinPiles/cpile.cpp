/* To do local test, create input file in.txt,
 * compile with command,
 * $ g++ -D __LOCAL xxx.cpp
 */
#include<iostream>

using namespace std;

#ifdef __LOCAL
#include<fstream>
ifstream fIn("in.txt");
#define cin fIn
#endif

int main() {
    int t;

    cin >> t;
    for (int i = 0; i < t; ++i) {
        int a, b;
        cin >> a >> b;

        if (a == 0 && b == 0) {
            cout << "YES" << endl;;
            continue;
        } else if (a == 0 || b == 0) {
            cout << "NO" << endl;;
            continue;
        }

        int aRem = a % 3;
        int bRem = b % 3;
        if ((aRem == 0 && bRem == 0) ||
            (aRem == 1 && bRem == 2) ||
            (aRem == 2 && bRem == 1)) {
            if ((a > b && a / 2 > b) ||
               (a < b && b / 2 > a)) {
                cout << "NO" << endl;
                continue;
            }
            cout << "YES" << endl;
        } else {
            cout << "NO" << endl;
        }
    }
    return 0;
}
