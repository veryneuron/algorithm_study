#include <string>
#include <vector>
#include <queue>

using namespace std;

int solution(vector<int> scoville, int K) {
    int answer = 0;
    priority_queue<int, vector<int>, greater<int>> heaptree;

    for (auto i : scoville) heaptree.push(i);

    while(heaptree.top() < K) {

        int least = heaptree.top();
        heaptree.pop();
        int sec_least = heaptree.top();
        heaptree.pop();

        int new_value = least + sec_least*2;

        heaptree.push(new_value);
        answer++;

        if (heaptree.size() == 1 && heaptree.top() < K) return -1;
    }

    return answer;
}