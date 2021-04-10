#include<fstream>
#include<unordered_map>
#include<iostream>
#include<cstdint>

using namespace std;
typedef unordered_map<int, int> umap;

//#define _submit

#ifdef _submit
#define fIn cin
#define fOut cout
#else
ifstream fIn("subarry_div.in");
ofstream fOut("subarry_div.out");
#endif

int main() {
    int n;
    fIn >> n;

    umap remMap;    // Remainder map: key: remainder, value: count
    remMap[0] = 0;
    uint64_t ret = 0;
    int preSum = 0;

    for (int i = 0; i < n; ++i) {
        int nextNum;
        fIn >> nextNum;
        preSum += nextNum;
        int remainder = preSum % n;
        if (remainder == 0)
            ret++;

        if (remMap.find(remainder) != remMap.end()) {
            ret += remMap[remainder];
        }
        remMap[remainder]++;
    }

    fOut << ret << endl;
    return 0;
}
