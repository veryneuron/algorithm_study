#include <string>
#include <vector>
#include <deque>
#include <iostream>

using namespace std;

int result;

void DFS ( deque<int> numbers, int target, int check) {

    if (numbers.empty()) {
        if (check == target) result++;
        return;
    }

    deque<int> numbers2(numbers);

    int temp = check;

    check = check + numbers.front();
    numbers.pop_front();

    DFS(numbers, target, check);

    temp = temp - numbers2.front();
    numbers2.pop_front();

    DFS(numbers2, target, temp);

}

int solution(vector<int> numbers, int target) {
    int answer = 0;
    int check(0);

    deque<int> search;

    for (auto i : numbers) search.push_back(i);

    DFS(search, target, check);

    return result;
}

int main() {
    int check(0), result(0), i(0);
    vector<int> num= {1, 1};
    int target = 0;

    i = solution(num, target);

    cout<<i<<endl;
}