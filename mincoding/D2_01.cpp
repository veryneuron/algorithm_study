#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct Edge {
    int a;
    int b;
    int cost;

    bool operator<(Edge other) {
        if (cost < other.cost) return true;
        return false;
    }
};

vector<Edge> graph;
int parents[10001];

int Find(int now) {
    if (parents[now] == now) return now;

    return parents[now] = Find(parents[now]);
}

void Union(int a, int b) {
    int pa = Find(a);
    int pb = Find(b);

    if (pa == pb) return;

    parents[pb] = pa;
}

int32_t main() {
    ios_base::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);

    int V, E;

    cin >> V >> E;

    for (int i = 0; i < E; i++) {
        int s, d, w;
        cin >> s >> d >> w;
        graph.push_back({s, d, w});
    }

    for (int i = 0; i <= V; i++) {
        parents[i] = i;
    }

    sort(graph.begin(), graph.end());

    int total(0), cnt(0);

    for (auto& g : graph) {
        int pa = Find(g.a);
        int pb = Find(g.b);
        if (pa == pb) continue;
        total += g.cost;
        Union(pa, pb);
        cnt++;
        if (cnt == V-1) break;
    }

    cout << total;

    return 0;
}