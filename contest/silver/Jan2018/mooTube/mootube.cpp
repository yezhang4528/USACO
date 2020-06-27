/*
 * vw: (N+1) * (N+1) matrix
 * row: node index
 * col: nodes to reach with weight as val in cell
 */
#include<iostream>
#include<fstream>
#include<vector>
#include<queue>

using namespace std;

struct Edge {
    int d;
    int w;
    Edge(int a, int b): d(a), w(b) {}
};

int N, Q;
vector<vector<Edge>> edges;
queue<int> nodes;

void printMatrix() {
    for (int i = 1; i <= N; i++) {
        for (auto e : edges[i])
            cout << i << " " << e.d << " " << e.w << ", ";
        cout << endl;
    }
}

int calculateVideos(int s, int threshold) {
    int ret = 0;
    nodes.push(s);
    vector<bool> visited(N+1);
    visited[s] = true;
    while (!nodes.empty()) {
        int from = nodes.front();
        nodes.pop();
        for (auto edge: edges[from]) {
            if (!visited[edge.d] && edge.w >= threshold) {
                visited[edge.d] = true;
                ret++;
                nodes.push(edge.d);
            }
        }
    }
    return ret;
}

int main()
{
    ifstream fin("mootube.in");

    fin >> N >> Q;
    edges.resize(N+1);
    int i;

    for (i = 0; i < N - 1; i++) {
        int p, q, r;
        fin >> p >> q >> r;
        Edge e1(q, r);
        edges[p].push_back(e1);
        Edge e2(p, r);
        edges[q].push_back(e2);
    } 
    //printMatrix();
    //cout << endl;

    ofstream fout("mootube.out");
    for (i = 0; i < Q; i++) {
        int k, v;
        fin >> k >> v;
        int result = calculateVideos(v, k);
        fout << result << endl;
    }

    return 0;
}
