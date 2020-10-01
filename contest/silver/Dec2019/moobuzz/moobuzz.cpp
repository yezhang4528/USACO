#include<iostream>
#include<fstream>

using namespace std;

int main() {
    ifstream fin("moobuzz.in");
    int N;
    fin >> N;

    // For every 15 numbers, there are 8 real numbers, 7 moos.
    // Looking for Nth number, N / 8 = K gives us the set of numbers,
    // The set of number starts at K*15+1, N % 8 gives us the offset of the number

    int K = N / 8;
    int offset = N % 8;

    long long num = (long long)K * 15 + 1;

    for (int i = 0; i < 15; ++i) {
        if (offset > 0 && (num % 3 && num % 5))
            --offset;
        if (offset == 0)
            break;
        ++num;
    }

    ofstream fout("moobuzz.out");
    fout << num << endl;
    return 0;
}
