#include <string>
#include <vector>
#include <iostream>

using namespace std;

int solution(int n, vector<int> lost, vector<int> reserve) {

    vector<int> cloth(n, 1);
    int answer = 0;

    for (auto i : lost) cloth[i-1]--;
    for (auto i : reserve) cloth[i-1]++;

    for (int i = 0; i < n; i++) {
        if (cloth[i] == 2) {
            if (i > 0 && cloth[i-1] == 0) {
                cloth[i]--;
                cloth[i-1]++;
            }
        if (cloth[i] == 2) {
            if (i < n-1 && cloth[i+1] == 0) {
                cloth[i]--;
                cloth[i+1]++;
            }
        }

        }
    }

    for (auto i : cloth) {
        if (i != 0) answer++;
    }


    return answer;
}

int main() {

    vector<int> first = {1, 3, 5};
    vector<int> second = {2, 4, 6};

    int result = solution(6, first, second);

    cout<<result<<endl;

    return 0;
}