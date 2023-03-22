#include <iostream>

using namespace std;

int32_t main() {
    ios_base::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);

    int N, M;
    cin >> N >> M;
    int numbers[100001] = {};
    for (int i = 1; i <= N; i++) {
        int input;
        cin >> input;
        numbers[i] = numbers[i-1] + input;
    }
    for (int i = 0; i < M; i++) {
        int from, to;
        cin >> from >> to;
        cout << numbers[to] - numbers[from-1] << "\n";
    }
    

    return 0;
}