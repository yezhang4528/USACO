#include<iostream>
#include<fstream>
#include<vector>

using namespace std;
int N, M;
vector<vector<bool>> visited(250, vector<bool>(250));
int best = 251;
vector<int> tiles(250);
vector<int> limits(250);
vector<int> steps(250);

void travel(int start, int curBoot) {
    if (visited[start][curBoot])
        return;

    visited[start][curBoot] = true;
    if (start == N - 1) {
        // With current Boot, we reached destination. All previous ones got discarded.
        best = min(best, curBoot);
        return;
    }

    // With curBoot, from the starting point, try to go as further as possible.
    for (int i = start + 1; i < N && i - start <= steps[curBoot]; ++i) {
        if (tiles[i] <= limits[curBoot])
            travel(i, curBoot);
    }

    for (int j = curBoot +1; j < M; ++j) {
        if (tiles[start] <= limits[j])
            travel(start, j);
    }
}

int main() {
    ifstream fin("snowboots.in");
    fin >> N >> M;

    for (int i = 0; i < N; ++i)
        fin >> tiles[i];

    for (int i = 0; i < M; ++i)
        fin >> limits[i] >> steps[i];

    travel(0, 0);

    ofstream fout("snowboots.out");
    fout << best << endl;

    return 0;
}
