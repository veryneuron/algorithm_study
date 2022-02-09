#include <string>
#include <vector>
#include <iostream>

using namespace std;

vector<int> solution(vector<int> progresses, vector<int> speeds) {

    vector<int> round, temp;
    vector<vector<int>> stack;
    vector<int> answer;

    int index(0),counter(0);

    for (int i = 0; i < progresses.size(); ++i) {
        round.push_back((100 - progresses[i]) / speeds[i]);
        if (((100-progresses[i]) % speeds[i]) != 0) round[i]++;
    }

    while (index < round.size()) {

        temp.push_back(round[index]);
        counter = round[index];
        if (++index < round.size()) {
            while(round[index] <= counter) {
                temp.push_back(round[index]);
                counter = counter - round[index];
                index++;
            }
        }
        stack.push_back(temp);
        temp.clear();
    }
    

    for (auto result : stack) answer.push_back(result.size());

    return answer;
}

int main() {
    vector<int> progress = {93, 30, 55};
    vector<int> speed = {1, 30, 5};

    for (auto i : solution(progress, speed)) cout<< i << endl;

    return 0;

}