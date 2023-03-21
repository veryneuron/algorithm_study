#include <iostream>
#include <cmath>

using namespace std;

char path[4];
string password;
int cnt;
int ans;

void func(int level) {
    if (level == 4) {
        cnt++;
        string temp = "";
        for (int i = 0; i < 4; i++) temp += path[i];
        if (temp == password) ans = cnt;
        return;
    }
    for (char i = 'A'; i <= 'Z'; i++) {
        if (ans != 0) continue;
        path[level] = i;
        func(level + 1);
        path[level] = 0;
    }
}

int32_t main() {
    ios_base::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);

    int N;
    cin >> N;
    for (int i = 0; i < N; i++) {
        cin >> password;
        fill_n(path, 4, 0);
        cnt = 0;
        ans = 0;
        func(0);
        cout << ans << "\n";
    }
    return 0;
}