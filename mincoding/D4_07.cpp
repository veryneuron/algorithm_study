#include <iostream>
#include <vector>
using namespace std;
int N; //세로 크기 
int M; //가로 크기
vector<vector<int>> MAP; 
vector<vector<int>> visited;
int ydir[] = { -1, -2, -1, 1, 2, 1 };
int xdir[] = { -1, 0, 1, 1, 0, -1 };

//특수 모양 Y자 방향 배열
int Y[][2] = {
	{0, 0},
	{-1, -1},
	{-1, 1},
	{2, 0}
};
// 특수 모양 역 Y자 방향 배열 
int reverseY[][2] = {
	{0, 0},
	{-2, 0},
	{1, -1},
	{1, 1}
};

int ans = -21e8;

void dfs(int y, int x, int cnt, int sum) {
	// 기저 조건
	if(cnt == 4) {
		if(sum > ans)
			ans = sum;
		return; 
	}
	// 재귀 구성
	for(int i = 0; i < 6; i++) {
		int ny = y + ydir[i];
		int nx = x + xdir[i];
		if(ny < 0 || nx < 0 || ny >= N*2 || nx >= M)
			continue;
		if(visited[ny][nx] == 1)
			continue;
		if(MAP[ny][nx] == 0)
			continue;
		visited[ny][nx] = 1;
		dfs(ny, nx, cnt + 1, sum + MAP[ny][nx]);
		visited[ny][nx] = 0; 
	}
}

void stamp(int y, int x, int dir[][2]) {
	int sum = 0; 
	for(int i = 0; i < 4; i++) {
		int ny = y + dir[i][0];
		int nx = x + dir[i][1]; 
		if(ny < 0 || nx < 0 || ny >= N*2 || nx >= M || MAP[ny][nx] == 0)
			return; 
		sum += MAP[ny][nx]; 
	}
	if(sum > ans)
		ans = sum; 
}

int main() {
    cin >> N >> M;
    MAP = vector<vector<int>>(N*2, vector<int>(M));
    visited = vector<vector<int>>(N*2, vector<int>(M));
	for(int i = 0; i < N * 2; i+=2) {
		for(int j = 0; j < M; j++) {
			if(j % 2 == 0)
				cin >> MAP[i][j];
			else
				cin >> MAP[i+1][j];
		}
	}
	for(int i = 0; i < N*2; i++) {
		for(int j = 0; j < M; j++) {
			if(visited[i][j] == 0 && MAP[i][j] != 0) {
				visited[i][j] = 1; 
				dfs(i, j, 1, MAP[i][j]);
				stamp(i, j, Y);
				stamp(i, j, reverseY); 
			}
		}
	}
    cout << ans;
    return 0;
}