#include <iostream>

using namespace std;

int indian[100];
int is_new[100];
int count_group;

int find(int target) {
    if (indian[target] == target) return target;

    return indian[target] = find(indian[target]);
}


void make_union(int parent, int child) {
    int parent_of_parent = find(parent);
    int parent_of_child = find(child);

    if (is_new[parent] == 0) {
        is_new[parent]++;
        count_group++;
    }

    if (is_new[child] == 0) {
        is_new[child]++;
        count_group++;
    }

    if (parent_of_parent == parent_of_child) return;

    indian[parent_of_child] = parent_of_parent;

    count_group--;
}

int32_t main() {
    ios_base::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);

    int N;

    cin >> N;

    for (int i = (int)'A'; i <= (int)'Z'; i++) {
        indian[i] = i;
    }

    for (int i = 0; i < N; i++) {
        char A, B;
        cin >> A >> B;
        make_union((int)A, (int)B);
    }

    int count_solo(0);

    for (int i = (int)'A'; i <= (int)'Z'; i++) {
        if (is_new[i] == 0) count_solo++;
    }

    cout << count_group << "\n" << count_solo << "\n";

    

    return 0;
}