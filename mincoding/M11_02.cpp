#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>

using namespace std;

struct Cor {
    int y;
    int x;

    bool operator==(Cor other) {
        if (y == other.y && x == other.x) return true;

        return false;
    }
};

struct Node {
    Cor from;
    Cor to;
    int cost;

    bool operator<(Node other) {
        if (cost < other.cost) return true;
        if (cost > other.cost) return false;

        return false;
    }
};

vector<Node> farms;
vector<Cor> MAP;
Cor group[1001][1001];

int is_new[1001][1001];
int grp_cnt;

Cor find(Cor target) {
    if (group[target.y][target.x] == target) return target;
    return group[target.y][target.x] = find(group[target.y][target.x]);
}


void make_union(Cor parent, Cor child) {
    Cor A = find(parent);
    Cor B = find(child);
    if (A == B) return;

    group[B.y][B.x] = A;

}


int32_t main() {
    ios_base::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);

    int N, K;

    cin >> N >> K;

    for (int i = 0; i < N; i++) {
        int y, x;

        cin >> y >> x;
        MAP.push_back({y, x});
    }

    for (auto& m1 : MAP) {
        for (auto& m2 : MAP) {
            if (m1.y == m2.y && m1.x == m2.x) continue;
            int cal_cost = pow(m1.x - m2.x, 2) + pow (m1.y - m2.y, 2);
            if (cal_cost < K) continue;
            farms.push_back({m1, m2, cal_cost});
        }
    }

    for (int i = 0; i <= 1000; i++) for (int j = 0; j <= 1000; j++) group[i][j] = {i , j};

    sort(farms.begin(), farms.end());

    int total_cost(0);
    int cnt(0);
    int flag(0);
    for (auto& farm : farms) {
        if (find(farm.from) == find(farm.to)) continue;
        make_union(farm.from, farm.to);
        total_cost += farm.cost;
        cnt++;
        if (cnt == N-1) {
            flag = 1;
            break;
        }
    }

    if (flag == 1) {
        cout << total_cost;
    } else {
        cout << -1;
    }


    return 0;
}