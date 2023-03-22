#include <iostream>
#include <cmath>
#include <algorithm>

using namespace std;

bool option(int A, int B) {
    if (A > B) return true;
    if (A < B) return false;
    return false;
}

int32_t main() {
    ios_base::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);

    int N;
    cin >> N;
    
    int arr[26] = {};
    for (int i = 0; i < N; i++) {
        string input;
        cin >> input;
        for (int j = 0; j < input.size(); j++) {
            arr[input[j]-'A'] += pow(10, input.size() - j - 1);
        }
    }

    sort(arr, arr+26, option);

    int sum(0);

    for (int i = 0; i < 10; i++) {
        sum += (9-i)*arr[i];
    }

    cout << sum;


    return 0;
}