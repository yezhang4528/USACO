#include<iostream>
#include<string>
#include<stack>
#include<vector>
#include<algorithm>

using namespace std;

#define _SUBMIT

#ifdef _SUBMIT
#define fIn cin
#else
#include<fstream>
ifstream fIn("nonp.in");
#endif

int N;
string paintStr;

void calSum(vector<int>& pSum) {
    stack<char> st;
    for (int i = 1; i <= N; ++i) {
        pSum[i] = pSum[i-1];
        while (!st.empty() && st.top() > paintStr[i])
            st.pop();
        if (st.empty() || st.top() < paintStr[i]) {
            st.push(paintStr[i]);
            pSum[i]++;

        }
    }
}

int main() {
    int Q;
    fIn >> N >> Q;

    fIn >> paintStr;
    paintStr = 'a' + paintStr;

    vector<int> pSum;
    vector<int> sSum;
    pSum.resize(N+2);
    sSum.resize(N+2);

    calSum(pSum);
    reverse(paintStr.begin()+1, paintStr.end());
    calSum(sSum);

    for (int i = 0; i < Q; ++i) {
        int start, end;
        fIn >> start >> end;

        cout << pSum[start-1] + sSum[N-end] << endl;
    }
    return 0;
}
