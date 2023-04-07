#include <iostream>

using namespace std;

int arr[100001];
long long tree[100001 * 4];

long long merge(long long left, long long right) {
    return left + right;
}

long long init(int start, int end, int node) {
    if (start == end) return tree[node] = arr[start];

    int mid = (start + end) / 2;
    long long left_val = init(start, mid, node*2);
    long long right_val = init(mid+1, end, node*2+1);
    return tree[node] = merge(left_val, right_val);
}

long long query(int start, int end, int node, int left, int right) {
    if (start > right || end < left) return 0;
    if (left <= start && end <= right) return tree[node];

    int mid = (start + end) / 2;

    long long left_val = query(start, mid, node*2, left, right);
    long long right_val = query(mid+1, end, node*2+1, left, right);

    return merge(left_val, right_val);
}

long long update(int start, int end, int node, int idx, int val) {
    if (idx < start || idx > end) return tree[node];
    if (start == end) return tree[node] = val;

    int mid = (start + end) / 2;

    long long left_val = update(start, mid, node*2, idx, val);
    long long right_val = update(mid+1, end, node*2+1, idx, val);

    return tree[node] = merge(left_val, right_val);
}


int32_t main() {
    ios_base::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);

    int N, Q;
    cin >> N >> Q;


    for (int i = 1; i <= N; i++) cin >> arr[i];
    init(1, N, 1);
    for (int i = 0; i < Q; i++) {
        int cmd, a, b;
        cin >> cmd >> a >> b;

        if (cmd == 1) {
            update(1, N, 1, a, b);
        } else {
            cout << query(1, N, 1, a, b) << '\n';
        }
    }



    return 0;
}