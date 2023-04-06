#include <iostream>

using namespace std;

int arr[1000001];
int tree[1000001 * 4];

int merge(int left, int right) {
    return min(left, right);
}

int init(int start, int end, int node) {
    if (start == end) return tree[node] = arr[start];

    int mid = (start + end) / 2;
    int left_val = init(start, mid, node*2);
    int right_val = init(mid+1, end, node*2+1);

    return tree[node] = merge(left_val, right_val);
}

int query(int start, int end, int node, int left, int right) {
    if (start > right || end < left) return 21e8;
    if (left <= start && end <= right) return tree[node];

    int mid = (start + end) / 2;
    int left_val = query(start, mid, node*2, left, right);
    int right_val = query(mid+1, end, node*2+1, left, right);

    return merge(left_val, right_val);
}

int32_t main() {
    ios_base::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);

    int N, M;
    cin >> N >> M;

    for (int i = 1; i <= N; i++) cin >> arr[i];

    init(1, N, 1);

    for (int i = 0; i < M; i++) {
        int s, e;
        cin >> s >> e;
        cout << query(1, N, 1, s, e) << '\n';
    }
    

    return 0;
}