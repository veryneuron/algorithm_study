#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
#include <cstring>

using namespace std;

struct Pos {
    int y, x;
};

struct Edge {
    int a;
    int b;
    int cost;

    bool operator <(Edge other) {
        if (cost < other.cost) return true;
        return false;
    }
};

int Y, X;
char MAP[50][50];
int Num[50][50];
int n;
vector<Edge> al;
vector<int> parent;

void bfs(int y, int x) {
    queue<Pos> q;
    q.push({y, x});

    int visited[50][50] = {};
    visited[y][x] = 1;

    int ydir[] = {-1, 1, 0, 0};
    int xdir[] = {0, 0, -1, 1};

    while (!q.empty()) {
        Pos now = q.front(); q.pop();

        if (Num[now.y][now.x] != 0 && Num[now.y][now.x] != Num[y][x]) {
            al.push_back({Num[y][x], Num[now.y][now.x], visited[now.y][now.x] - 1});
        }

        for (int i = 0; i < 4; i++) {
            int ny = now.y + ydir[i];
            int nx = now.x + xdir[i];

            if (ny < 0 || nx < 0 || ny >= Y || nx >= X) continue;
            if (visited[ny][nx] != 0) continue;
            if (MAP[ny][nx] == '#') continue;
            visited[ny][nx] = visited[now.y][now.x] + 1;
            q.push({ny, nx});
        }
    }
}

int Find(int now) {
    if (parent[now] == now) return now;
    return parent[now] = Find(parent[now]);
}

void Union(int a, int b) {
    int pa = Find(a);
    int pb = Find(b);

    if (pa == pb) return;

    parent[pb] = pa;
}

int kruskal() {
    sort(al.begin(), al.end());
    int sum = 0;
    for (int i = 0; i < al.size(); i++) {
        Edge now = al[i];
        if (Find(now.a) == Find(now.b)) continue;
        sum += now.cost;
        Union(now.a, now.b);
    }
    return sum;
}

int32_t main() {
    ios_base::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);

    int T;
    cin >> T;
    for (int tc = 1; tc <= T; tc++) {
        al.clear();
        memset(Num, 0, sizeof(Num));
        cin >> X >> Y;
        n = 1;
        for (int i = 0; i < Y; i++) {
            for (int j = 0; j < X; j++) {
                cin >> MAP[i][j];
                if (MAP[i][j] == 'A' || MAP[i][j] == 'S') {
                    Num[i][j] = n;
                    n++;
                }
            }
        }
        for (int i = 0; i < Y; i++) {
            for (int j = 0; j < X; j++) {
                if (Num[i][j] != 0) {
                    bfs(i, j);
                }
            }
        }
        parent = vector<int>(n+1);
            for (int i = 0; i <= n; i++) {
                parent[i] = i;
            }

        cout << kruskal() << '\n';
    }

    return 0;
}