#include <iostream>
#include <cstring>

using namespace std;

int N;
int arr[100000];
int temp[100000];

void merge(int left, int right) {
    memset(temp, 0, sizeof(temp));
    int mid = (left + right) / 2;
    int left_point = left;
    int right_point = mid + 1;
    int temp_idx = left;

    while (left_point <= mid && right_point <= right) {
        if (arr[left_point] < arr[right_point]) {
            temp[temp_idx++] = arr[left_point++];
        } else {
            temp[temp_idx++] = arr[right_point++];
        }
    }

    if (left_point > mid) {
        for (int i = right_point; i <= right; i++) {
            temp[temp_idx++] = arr[i];
        }
    } else {
        for (int i = left_point; i <= mid; i++) {
            temp[temp_idx++] = arr[i];
        }
    }

    for (int i = left; i <= right; i++) {
        arr[i] = temp[i];
    }

}

void mergesort(int left, int right) {
    if (left >= right) return;

    int mid = (left + right) / 2;

    mergesort(left, mid);
    mergesort(mid+1, right);
    merge(left, right);
    for (int i = left; i <= right; i++) {
        cout << arr[i] << " ";
    }

    cout << '\n';
}

int32_t main() {
    ios_base::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);

    cin >> N;
    for (int i = 0; i < N; i++) {
        cin >> arr[i];
    }
    mergesort(0, N-1);

    return 0;
}