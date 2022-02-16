// 9:56
#include <string>
#include <vector>
#include <unordered_map>
#include <iostream>

using namespace std;

bool solution(vector<string> phone_book) {
    bool answer = true;

    unordered_map<string, bool> num_table;

    for (auto &num : phone_book) num_table.insert({num, true});
    
    for (int i=0; i<phone_book.size(); ++i) {
        for (int j=1; j<=20; ++j) {
            if (phone_book[i].size() <= j) break;
            if (num_table.find(phone_book[i].substr(0, j)) != num_table.end()) return false;
        }
    }
    return answer;
}

int main() {
    vector<string> test = {"1195524421", "97674223", "119"};

    bool answ = solution(test);

    cout<<answ<<endl;

}