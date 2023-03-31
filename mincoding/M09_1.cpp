#include <iostream>

using namespace std;

int group[1001] = {};

int find(int target) {
    if (group[target] == target) return target;

    int parent = find(group[target]);
    
    group[target] = parent;

    return parent;
}

void make_union(int parent, int child) {
    int parent_of_parent = find(parent);
    int parent_of_child = find(child);

    if (parent_of_parent == parent_of_child) return;

    group[parent_of_child] = parent_of_parent;
}

int32_t main() {
    ios_base::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);

    int N, Q;


    cin >> N >> Q;

    for (int i = 1; i <= N; i++) {
        group[i] = i;
    }

    for (int i = 0; i < Q; i++) {
        int query, A, B;
        cin >> query >> A >> B;
        if (query == 1) {
            make_union(A, B);
        } else {
            if (find(A) == find(B)) {
                cout << "YES" << "\n";
            } else {
                cout << "NO" << "\n";
            }
        }
    }

    return 0;
}