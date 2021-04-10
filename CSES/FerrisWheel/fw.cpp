/* Ferris Wheel, https://cses.fi/problemset/task/1090 */

#include<iostream>
#include<vector>
#include<fstream>

using namespace std;

#ifdef __LOCAL
ifstream fin("fw.in");
#define cin fin
#endif

int main() {
    int n, x;
    vector<int> cw; // Children's weight
    int gCount = 0;
    int front = 0, back;

    cin >> n >> x;
    front = 0;
    back = n - 1;
    cw.resize(n);
    for (int i = 0; i < n; ++i) {
        cin >> cw[i];
    }
    sort(cw.begin(), cw.end());
    return 0;
}
