#include <string>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

int solution(int n, vector<vector<int>> edge) {
    int answer = 0;

    vector<vector<int>> graph(n+1);
    vector<int> dist(n+1);

    for (auto node : edge) {
        graph[node.front()].push_back(node.back());
        graph[node.back()].push_back(node.front());
    }

    queue<int> q;
    dist[1] = 1;

    q.push(1);

    while(!q.empty()) {

        int now = q.front();
        q.pop();
        for (auto next : graph[now]) {
            if (dist[next] == 0) {
                q.push(next);
                dist[next] = dist[now] + 1;
            }
        }
    }

    int maxvalue = *max_element(dist.begin(),dist.end());

    for (auto i : dist) if (i == maxvalue) answer++;
    
    return answer;
}