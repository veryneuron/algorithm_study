#include <string>
#include <vector>
#include <set>
#include <cmath>

using namespace std;

int num_N;
set<int> tree[9];

set<int> dp(int depth) {
    if (!tree[depth].empty()) return tree[depth];

    int base_num = 0;

    for (int i=0; i<depth; ++i) base_num += num_N*(int)pow(10, i);
    tree[depth].insert(base_num);

    for (int i=1; i < depth; ++i) {
        auto temp_1 = dp(i);
        auto temp_2 = dp(depth - i);

        for (auto itr_1 : temp_1) {
            for (auto itr_2 : temp_2) {
                tree[depth].insert(itr_1 + itr_2);
                tree[depth].insert(itr_1 - itr_2);
                tree[depth].insert(itr_1 * itr_2);
                if (itr_2 != 0) tree[depth].insert(itr_1 / itr_2);
            }
        }
    }

    return tree[depth];
}



int solution(int N, int number) {
    int answer = -1;

    num_N = N;

    for (int i=1; i<=8; ++i) {
        dp(i);
        if (tree[i].find(number) != tree[i].end()) return i;
    }
    

    return answer;
}