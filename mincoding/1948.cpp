#include <iostream>
#include <vector>
#include <queue>

struct road {
    int to;
    long time;

};

using namespace std;

int32_t main() {
    ios_base::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);

    int n, m;
    cin >> n >> m;
    vector<road> road_list[10001];
    vector<road> reverse_road_list[10001];

    int indegree[10001] = {};
    for (int i = 1; i <= m; i++) {
        int from, to;
        long time;
        cin >> from >> to >> time;
        road_list[from].push_back({to, time});
        reverse_road_list[to].push_back({from, time});
        indegree[to]++;
    }

    queue<int> q;

    int start, end;

    cin >> start >> end;

    int dist[10001] = {};
    q.push(start);

    while (!q.empty()) {
        int cur = q.front(); q.pop();
        for (auto& next : road_list[cur]) {
            if (dist[next.to] < dist[cur] + next.time) {
                dist[next.to] = dist[cur] + next.time;
            }
            indegree[next.to]--;
            if (indegree[next.to] == 0) q.push(next.to);
        }
    }

    cout << dist[end] << '\n';

    q.push(end);
    int ans(0);
    int visited[10001] = {};
    while(!q.empty()) {
        int cur = q.front(); q.pop();
        if (visited[cur] == 1) continue;
        visited[cur] = 1;
        for (auto& pre : reverse_road_list[cur]) {
            if (dist[cur] == dist[pre.to] + pre.time) {
                ans++;
                q.push(pre.to);
            }
        }
    }

    cout << ans;

    return 0;
}