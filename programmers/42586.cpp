#include <string>
#include <vector>
#include <iostream>
#include <deque>

using namespace std;

vector<int> solution(vector<int> progresses, vector<int> speeds) {

    deque<int> round;
    vector<int> answer;

    for (int i = 0; i < progresses.size(); ++i) {
        round.push_back((100 - progresses[i]) / speeds[i]);
        if (((100-progresses[i]) % speeds[i]) != 0) round[i]++;
    }

    while (!round.empty()) {
        int temp = round.front();
        int func(1);
        round.pop_front();

        auto itr = round.begin();
        
        while ((!round.empty()) && (round.front() <= temp)) {
            round.pop_front();
            func++;
        }
        
        answer.push_back(func);
    }
    

    return answer;
}

int main() {
    vector<int> progress = {95, 90, 99, 99, 80, 99};
    vector<int> speed = {1, 1, 1, 1, 1, 1};

    for (auto i : solution(progress, speed)) cout<< i << endl;

    return 0;

}