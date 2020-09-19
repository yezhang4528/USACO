#include<iostream>
#include<fstream>
#include<vector>
#include<algorithm>

using namespace std;

#define MAX_NUM 250

typedef pair<int, int> pi;

vector<int> tiles(MAX_NUM);
vector<pi> boots(MAX_NUM);  // boot.first: inches upto; boot.second: step can go
vector<vector<bool>> visited(MAX_NUM, vector<bool>(MAX_NUM));
int N, B;   // Number of tiles, number of boots

int DPsolution() {
    int i, j;
    visited[0][0] = true;
    for (i = 0; i < B; ++i) { // Loop through boots
        for (j = 0; j < N; ++j) { // Loop through tiles
            if (tiles[j] > boots[i].first)    // Snow too deep for the boot
                continue;
            for (int n = 0; n < j; ++n) { // Try to reach the ith tile from earlier steps, column down
                if (visited[i][n] && n + boots[i].second >= j) {
                   visited[i][j] = true;
                   break;
                }
            }

            // No need to walk, just changing boots can reach this step. Snow depth is guaranteed
            // by first "if" statement.
            for (int b = 0; b < i; ++b) {
                if (visited[b][j])
                    visited[i][j] = true;
            }

            if (j == N-1 && visited[i][j] == true)
                return i;
        }
    }

    return i;
}

int main() {
    ifstream fin("snowboots.in");
    fin >> N >> B;

    for (int i = 0; i < N; ++i)
        fin >> tiles[i];

    for (int i = 0; i < B; ++i)
        fin >> boots[i].first >> boots[i].second;

    ofstream fout("snowboots.out");
    fout << DPsolution() << endl;;
    
    return 0;
}
