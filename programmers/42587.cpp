// 3:32-4:10
#include <string>
#include <vector>
#include <deque>

using namespace std;

int solution(vector<int> priorities, int location) {
    int answer = 1;
    deque<int> q;
    bool flag;
    int temp;

    for (int i : priorities) q.push_back(i);

    while (!q.empty()) {
        flag = false;
        for (int j : q) {
            if (j > q.front()) flag = true; // max_element로 대체가능했음!!
        }
        if (flag == true) {
            temp = q.front();
            q.pop_front();
            q.push_back(temp);
            if (location == 0) location = q.size();
            location--;
        }
        else {
            if (location == 0) return answer;
            q.pop_front();
            location--;
            answer++;
        }

    }

}