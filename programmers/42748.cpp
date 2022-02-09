#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> array, vector<vector<int>> commands) {
    vector<int> answer, temp;

    for (auto order : commands) {
        for (int i=order[0]-1; i < order[1]; i++){
            temp.push_back(array[i]);
        }

        sort(temp.begin(),temp.end());

        answer.push_back(temp[order[2]-1]);

        temp.clear();

    }


    return answer;
}