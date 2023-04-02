#include <iostream>
#define NUMBER 12

// source : https://m.blog.naver.com/ndb796/221282210534

using namespace std;

int values[] = {1, 9, 3, 8, 4, 5, 5, 9, 10, 3, 4, 5};
int tree[4 * NUMBER]; // 4를 곱하면 모든 범위를 커버할 수 있음. 갯수에 대해서 2의 제곱 형태의 길이를 가지기 때문임. 

int init(int start, int end, int node) {
    if (start == end) return tree[node] = values[start];
    int mid = (start + end) / 2;

    return tree[node] = init(start, mid, node*2) + init(mid+1, end, node*2+1);
}

int sum(int start, int end, int node, int left, int right) {
    if (left > end || right < start) return 0;

    if (left <= start && end <= right) return tree[node];

    int mid = (start + end) / 2;

    return sum(start, mid, node*2, left, right) + sum(mid+1, end, node*2+1, left, right);
}

void update(int start, int end, int node, int index, int diff) {

    if (index < start || index > end) return;
    tree[node] += diff;
    if (start == end) return;
    int mid = (start + end) / 2;

    update(start, mid, node*2, index, diff);
    update(mid+1, end, node*2+1, index, diff);
}

int32_t main() {
    ios_base::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);

    init(0, NUMBER-1, 1);

    cout << "0부터 12까지의 구간 합: " << sum(0, NUMBER - 1, 1, 0, 12) << '\n';
	// 구간 합 구하기 
	cout << "3부터 8까지의 구간 합: " << sum(0, NUMBER - 1, 1, 3, 8) << '\n';
	// 구간 합 갱신하기
	cout << "인덱스 5의 원소를 -5만큼 수정" << '\n';
	update(0, NUMBER - 1, 1, 5, -5); 
	// 구간 합 다시 구하기 
	cout << "3부터 8까지의 구간 합: " << sum(0, NUMBER - 1, 1, 3, 8) << '\n';
    
    return 0;
}