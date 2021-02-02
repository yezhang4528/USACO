#include<fstream>
#include<vector>

using namespace std;

typedef vector<int> vi; 
typedef vector<vi> vvi;  
#define FOR(a, b, c) for (int(a) = (b); (a) < (c); ++(a)) 

// Uncomment this line when submit / comment this line when test locally
ifstream fIn("bcount.in");
ofstream fOut("bcount.out");

int main() {
    vvi cowV(4);

    int N, Q;
    fIn >> N >> Q;
    cowV[1].resize(N + 1);
    cowV[2].resize(N + 1);
    cowV[3].resize(N + 1);

    FOR(i, 0, N) {
        int cow;
        fIn >> cow;
        cowV[1][i+1] = cowV[1][i];
        cowV[2][i+1] = cowV[2][i];
        cowV[3][i+1] = cowV[3][i];
        cowV[cow][i+1]++; 
    }

    FOR(i, 0, Q) {
        int start, end;
        fIn >> start >> end;
        fOut << cowV[1][end] - cowV[1][start-1] << " "
             << cowV[2][end] - cowV[2][start-1] << " "
             << cowV[3][end] - cowV[3][start-1] << endl;
    }
    
    return 0;
}
