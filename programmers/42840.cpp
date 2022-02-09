#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> answers) {
    vector<int> answer;

    vector<int> supo1 = {1, 2, 3, 4, 5};
    vector<int> supo2 = {2, 1, 2, 3, 2, 4, 2, 5};
    vector<int> supo3 = {3, 3, 1, 1, 2, 2, 4, 4, 5, 5};
    int counter(0);
    int score1(0), score2(0), score3(0);

    for (auto i : answers) {
        if (i == supo1[counter % supo1.size()]) score1++;
        if (i == supo2[counter % supo2.size()]) score2++;
        if (i == supo3[counter % supo3.size()]) score3++;
        counter++;        
    }
    vector<pair<int, int>> supo_result;
    supo_result.push_back(pair<int, int>(score1, 1));
    supo_result.push_back(pair<int, int>(score2, 2));
    supo_result.push_back(pair<int, int>(score3, 3));

    sort(supo_result.begin(),supo_result.end(), greater<>());

    answer.push_back(supo_result[0].second);
    if (supo_result[0].first == supo_result[1].first) answer.push_back(supo_result[1].second);
    if (supo_result[0].first == supo_result[2].first) answer.push_back(supo_result[2].second);

    sort(answer.begin(), answer.end());


    return answer;
}