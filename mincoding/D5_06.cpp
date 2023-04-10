#include <iostream>
#include <queue>
#define int long long

using namespace std;

int32_t main() {
    ios_base::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);

    priority_queue<int, vector<int>, greater<int>> pq;
    pq.push(1);
    int cnt = 1;
    int pre = 0;
    int arr[1502] = {};

    while (cnt <= 1500) {
        int now = pq.top(); pq.pop();

        if (pre == now) continue;
        arr[cnt] = now;
        pq.push(now * 2);
        pq.push(now * 3);
        pq.push(now * 5);
        cnt++;
        pre = now;
    }

    int N;
    cin >> N;

    for (int i = 0; i < N; i++) {
        int num;
        cin >> num;
        cout << arr[num] << " ";
    }
    return 0;
}