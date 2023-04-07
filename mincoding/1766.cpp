#include <iostream>
#include <queue>
#include <vector>

using namespace std;



int32_t main() {
    ios_base::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);

    int N, M;
    vector<int> graph[32001];
    int indegree[32001];

    cin >> N >> M;

    priority_queue<int, vector<int>, greater<int>> pq;

    for (int i = 0; i < M; i++) {
        int A, B;
        cin >> A >> B;
        graph[A].push_back(B);
        indegree[B]++;
    }

    for (int i = 1; i <= N; i++) {
        if (indegree[i] == 0) pq.push(i);
    }

    while (!pq.empty()) {
        int now = pq.top(); pq.pop();

        cout << now << " ";
        for (auto& next : graph[now]) {
            indegree[next]--;
            if (indegree[next] == 0) pq.push(next);
        }
    }


    return 0;
}