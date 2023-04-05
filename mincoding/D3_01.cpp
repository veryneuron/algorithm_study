#include <iostream>
#include <algorithm>
using namespace std;

int arr[100001];

int binarysearch(int left, int right, int target) {
    if (left > right) return -1;

    int mid = (left + right) / 2;

    if (arr[mid] == target) return 1;

    if (arr[mid] < target) {
        return binarysearch(mid+1, right, target);
    } else if (arr[mid] > target) {
        return binarysearch(left, mid-1, target);
    }

    return -1;
}


int32_t main() {
    ios_base::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);

    int N;
    cin >> N;
    for (int i = 0; i < N; i++) {
        cin >> arr[i];
    }

    sort(arr, arr+N);

    int K;
    cin >> K;
    for (int i = 0; i < K; i++) {
        int target;
        cin >> target;
        int found = binarysearch(0, N-1, target);
        if (found == 1) cout << "O";
        else cout << "X";
    }

    return 0;
}