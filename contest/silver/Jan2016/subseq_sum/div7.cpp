#include<fstream>
#include<vector>

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef vector<ll> vll;

#define MAX_POS 50001
#define DIVISOR 7

ifstream fIn("div7.in");
ofstream fOut("div7.out");

int main() {
    /* Vector to save pos of the same remainder first and last time appearance.
     * Then the numbers in between should add up to 7 mulipliers.
     */
    vi first(DIVISOR, MAX_POS), last(DIVISOR);
    long long sum = 0;

    int N;
    fIn >> N;
    for (int i = 1; i <= N; ++i) {
        int next, rem = 0;
        fIn >> next;
        sum += next;
        rem = sum % DIVISOR;
        first[rem] = min(first[rem], i);
        last[rem] = i;
    }

    int longest = 0;
    for (int i = 0; i < DIVISOR; ++i) {
        int curL = last[i] - first[i];
        if (curL > longest)
            longest = curL;
    }
    fOut << longest << endl;
    return 0;
}
