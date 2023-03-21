#include <iostream>

using namespace std;

int N;
int cnt;
int sum;
int DAT[51];
int path[51];

void func(int level) {
    if (sum > N) return;
    if (sum == N) {
        cnt++;
        return;
    }

    for (int i = 1; i <= N; i++) {
        if (DAT[i] >= 2) continue;
        if (level > 0 && i < path[level -1]) continue;
        DAT[i]++;
        path[level] = i;
        sum += i;
        func(level+1);
        DAT[i]--;
        path[level] = 0;
        sum -= i;
    }
}


int32_t main() {
    ios_base::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);

    cin >> N;

    func(0);

    cout << cnt;
    

    return 0;
}