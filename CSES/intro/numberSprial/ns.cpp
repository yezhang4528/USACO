#include<iostream>
#include<vector>

using namespace std;

#ifdef __LOCAL
#include<fstream>
ifstream fIn("in.txt");
#define cin fIn
#endif

#define MAXLEN 10^9

int main() {
    int t, x, y;

    cin >> t;

    for (int i = 0; i < t; ++i) {
        cin >> x >> y;

        long long res;
        /* The sprial grid even number square end at row starts,
         * while odd number square ends at column starts
         * if x > y, the number locates within x square grid
         * if y > x, the number locates within y square grid
         */
        long long xSQ = (long long)x * x;
        long long ySQ = (long long)y * y;
        if (x > y && !(x % 2) ) {  // x >= y, x even
            res = xSQ;
            res -= (y - 1);
        } else if ( x <= y && (y % 2)) { // x < y, y odd
            res = ySQ;
            res -= (x - 1);
        } else {
            res = (x > y)? xSQ : ySQ;
            if (x > y)
                res -= (x - 1) + (x - y);
            else
                res -= (y - 1) + (y - x);
        }
        
        cout << res << endl;
    }

    return 0;
}
