#include<iostream>
#include<fstream>
#include<vector>
#include<algorithm>

using namespace std;

void printVec(vector<pair<uint64_t, uint64_t>>& distV)
{
    for (auto v : distV)
        cout << v.first << " " << v.second << endl;
}

bool validateSocialDist(vector<pair<uint64_t, uint64_t>>& distV, uint64_t d, int cows)
{
    int cn = 0;         // cow number fits in social distancing d
    uint64_t nextStart = distV[0].first;

    for (auto p : distV) {
        int cowsFit = 0;
        if (p.second < nextStart)
            continue;

        if (p.second - p.first < d) {
            // Fit at most one cow
            cowsFit = 1;
            nextStart = (p.first > nextStart)? p.first + d : nextStart + d;
        } else if (nextStart <= p.first) {
            // Can fit more then one cow
            cowsFit = (p.second - p.first) / d + 1;
            nextStart = p.first + cowsFit * d;
        } else { // nextStart > p.first
            cowsFit = (p.second - nextStart) / d + 1;
            nextStart += cowsFit * d;
        }
        cn += cowsFit;

        if (cn >= cows)
            return true;
    }

    return false;
}

uint64_t findSocialDist(vector<pair<uint64_t, uint64_t>>& distV, int cows)
{
    uint64_t ret = 0;
    sort(distV.begin(), distV.end());
    int numPairs = distV.size();
    uint64_t low = distV[0].first, high = distV[numPairs-1].second;

    while (low < high) {
        uint64_t mid = low + (high - low)/2;

        if (validateSocialDist(distV, mid, cows)) {
            ret = mid;
            low = mid + 1;
        } else {
            high = mid - 1;
        }
    }
    return ret;
}

int main()
{
    ifstream fin;
    fin.open("socdist.in");
    int N, M;
    vector<pair<uint64_t, uint64_t>> distVec;

    fin >> N >> M;
    //cout << "N = " << N << ", M = " << M << endl; 
    for (int i = 0; i < M; i++) {
        uint64_t d1, d2;
        fin >> d1 >> d2;
        distVec.push_back(make_pair(d1, d2));
    }
    //printVec(distVec);
    fin.close();

    uint64_t largestDist = findSocialDist(distVec, N);
    ofstream fout;
    fout.open("socdist.out");
    fout << largestDist << endl;
    fout.close();

    return 0;
}
