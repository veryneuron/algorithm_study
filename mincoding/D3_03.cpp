#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

int K;
vector<int> tree;
int nodecnt;
int diff = 0;

int func(int node) {
    if (node*2 > nodecnt) return tree[node];

    int left = func(node * 2);
    int right = func(node * 2 + 1);

    diff += abs(left - right);
    return tree[node] += max(left, right);
}

int32_t main() {
    ios_base::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);
    
    cin >> K;
    nodecnt = pow(2, K+1) - 1;
    tree = vector<int>(nodecnt+1);
    int cur = 0;
    for (int i = 2; i <= nodecnt; i++) {
        cin >> tree[i];
        cur += tree[i];
    }
    
    func(1);
    cout << cur + diff;

    return 0;
}