#include<iostream>
#include<fstream>
#include<vector>
#include<queue>

using namespace std;

//#define DEBUG_ON

struct Pos
{
    int x;
    int y;
};

vector<vector<int>> distances;
vector<Pos>         pos;
vector<int>         powers;
int N;

#ifdef DEBUG_ON
void printMatrix() {
    // Print distances
    for (int i = 1; i <= N; i++) {
        cout << i << ": ";
        for (auto d : distances[i]) {
            cout << d << " ";
        }
        cout << endl;
    }
    // Print positions
    for (int i = 1; i <= N; i++)
        cout << i << ": " << pos[i].x << " " << pos[i].y << endl;

    // Print power
    for (int i = 1; i <= N; i++)
        cout << i << ": " << powers[i] << endl;

}
#endif

void calculateDistance() {
    for (int i = 1; i <= N; i++) {
        for (int j = 1; j <= N; j++) {
            if (i == j || distances[i][j] != 0)
                continue;
            distances[i][j] = (pos[i].x-pos[j].x) * (pos[i].x-pos[j].x) + (pos[i].y-pos[j].y)*(pos[i].y-pos[j].y);
            distances[j][i] = distances[i][j];
        }
    }
}

int bfs(int start) {
    int ret = 0;
    vector<bool> visited(N+1);
    queue<int> cows;
    cows.push(start);
    visited[start] = true;
    ret++;
    while (!cows.empty()) {
        int cur = cows.front();
        cows.pop();
        for (int i = 1; i <= N; i++) {
            if (powers[cur] >= distances[cur][i] && !visited[i]) {
                ret++;
                cows.push(i);
                visited[i] = true;
            }
        }
    }
    return ret;
}

int main()
{
    ifstream fin("moocast.in");
    fin >> N;

    distances.resize(N+1);
    powers.resize(N+1);
    for (int i = 0; i <= N; i++) {
        distances[i].resize(N+1);
    }

    pos.resize(N+1);
    for (int i = 1; i <= N; i++) {
        int x, y, p;
        fin >> x >> y >> p;
        pos[i].x = x;
        pos[i].y = y;
        powers[i] = p*p;
    }
    calculateDistance();
#ifdef DEBUG_ON
    printMatrix();
#endif

    int maxReach = 0;
    for (int i = 1; i <= N; i++) {
        maxReach = max(bfs(i), maxReach);
    }
    ofstream fout("moocast.out");
    fout << maxReach << endl;

    return 0;
}
