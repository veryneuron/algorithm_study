#include <string>
#include <vector>
#include <algorithm>

using namespace std;

long long solution(int n, vector<int> times) {
    long long answer = 0;
    long long low(1), mid(0), high(0);

    high = *max_element(times.begin(), times.end())*(long long)n;
    answer = high;

    while (low <= high) {
        mid = (low + high) / 2;

        long long humans(0);

        for (auto i : times) humans += (mid / (long long)i);
        
        if (n <= humans) {
            high = mid - 1;
            answer = mid;
        }
        else low = mid + 1;
    }


    return answer;
}