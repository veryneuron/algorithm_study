#include <iostream>
#include <algorithm>

using namespace std;

struct Node {
    int A;
    int B;
    int cost;
    bool operator<(Node other) {
        if (cost < other.cost) return true;
        if (cost > other.cost) return false;

        return false;
    }
};

int group[100001];

int find (int target) {
    if (group[target] == target) return target;

    return group[target] = find(group[target]);
}

void make_union(int parent, int child) {
    int parent_of_parent = find(parent);
    int parent_of_child = find(child);

    if (parent_of_parent == parent_of_child) return;

    group[parent_of_child] = parent_of_parent;
}

Node graph[100001];

int32_t main() {
    ios_base::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);

    int V, E;

    cin >> V >> E;

    for (int i = 1; i <= V; i++) {
        group[i] = i;
    }

    for (int i = 0; i < E; i++) {
        int A, B, C;
        cin >> A >> B >> C;

        graph[i] = {A, B, C};
    }

    sort(graph, graph+E);
    int total_cost(0);
    int cnt(0);

    for (int i = 0; i < E; i++) {
        if (find(graph[i].A) == find(graph[i].B)) continue;
        make_union(graph[i].A, graph[i].B);
        total_cost += graph[i].cost;
        if (cnt == V-1) break;
    }

    cout << total_cost;

    return 0;
}