#include <iostream>
#include <vector>
#define MAX 1001
#define LOG 11

//source : https://m.blog.naver.com/ndb796/221282478466

using namespace std;

int n, m, parent[MAX][LOG], depth[MAX];
bool check[MAX];
vector<int> a[MAX];

void dfs(int now, int dep) {
    check[now] = true;
    depth[now] = dep;

    for (int i = 0; i < a[now].size(); i++) {
        int nxt = a[now][i];
        if (check[nxt]) continue;
        parent[nxt][0] = now;
        dfs(nxt, dep+1);
    }
}

void setParent() {
    dfs(0, 0);

    for (int j = 1; j < LOG; j++) {
        for (int i = 0; i < n; i++) {
            parent[i][j] = parent[parent[i][j-1]][j-1];
        }
    }
}

int LCA(int x, int y) {

    if (depth[x] > depth[y]) {
        swap(x, y);
    }

    for (int i = LOG - 1; i >= 0; i--) {
        if (depth[y] - depth[x] >= (1 << i)) {
            y = parent[y][i];
        }
    }

    if (x == y) return x;
    for (int i = LOG - 1; i >= 0; i--) {
        if (parent[x][i] != parent[y][i])  {
            x = parent[x][i];
            y = parent[y][i];
        }
    }

    return parent[x][0];
}

int32_t main() {
    ios_base::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);

    n = 21;
	// 0과 1을 연결합니다.
	a[0].push_back(1);
	a[1].push_back(0);
	// 0과 2를 연결합니다.
	a[0].push_back(2);
	a[2].push_back(0);
	// 1과 3을 연결합니다.
	a[1].push_back(3);
	a[3].push_back(1);
	// 1과 4를 연결합니다.
	a[1].push_back(4);
	a[4].push_back(1);
	// 2와 5을 연결합니다.
	a[2].push_back(5);
	a[5].push_back(2);
	// 2와 6을 연결합니다.
	a[2].push_back(6);
	a[6].push_back(2);
	// 3과 7을 연결합니다.
	a[3].push_back(7);
	a[7].push_back(3);
	// 3과 8을 연결합니다.
	a[3].push_back(8);
	a[8].push_back(3);
	// 4와 9를 연결합니다.
	a[4].push_back(9);
	a[9].push_back(4);
	// 4와 10을 연결합니다.
	a[4].push_back(10);
	a[10].push_back(4);
	// 4와 11을 연결합니다.
	a[4].push_back(11);
	a[11].push_back(4);
	// 8과 12를 연결합니다.
	a[8].push_back(12);
	a[12].push_back(8);
	// 8과 13을 연결합니다.
	a[8].push_back(13);
	a[13].push_back(8);
	// 9와 14를 연결합니다.
	a[9].push_back(14);
	a[14].push_back(9);
	// 10과 15를 연결합니다.
	a[10].push_back(15);
	a[15].push_back(10);
	// 13과 16을 연결합니다.
	a[13].push_back(16);
	a[16].push_back(13);
	// 13과 17을 연결합니다.
	a[13].push_back(17);
	a[17].push_back(13);
	// 14와 18을 연결합니다.
	a[14].push_back(18);
	a[18].push_back(14);
	// 15와 19를 연결합니다.
	a[15].push_back(19);
	a[19].push_back(15);
	// 17과 20을 연결합니다.
	a[17].push_back(20);
	a[20].push_back(17);
	setParent();
	cout << "5와 7의 LCA: " << LCA(5, 7) << '\n';
	cout << "15와 20의 LCA: " << LCA(15, 20) << '\n';
	cout << "16과 17의 LCA: " << LCA(16, 17) << '\n';
	cout << "10과 9의 LCA: " << LCA(10, 9) << '\n';
	cout << "3과 17의 LCA: " << LCA(3, 17) << '\n';
	return 0;

    return 0;
}