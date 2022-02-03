#include <string>
#include <vector>
#include <unordered_map>

using namespace std;

string solution(vector<string> participant, vector<string> completion) {

    unordered_map<string, int> table;
    string answer = "";
    
    for (auto part : participant) table[part]++;
    for (auto part : completion) table[part]--;
    for (auto part : participant) {
        if (table[part] == 1) answer = part;
    }

    return answer;
}