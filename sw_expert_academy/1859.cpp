#include<iostream>
#include<deque>
#include<algorithm>

using namespace std;

int main(int argc, char** argv)
{
	int test_case;
	int T;
	
	cin>>T;

	for(test_case = 1; test_case <= T; ++test_case)
	{
        int N;
        cin >> N;
        int input;
        long long int wallet, revenue(0);
        deque<int> exp;

       for (int i=0; i<N; ++i) {
            cin >> input;
            exp.push_back(input);
        }

        while(1) {

            int max_idx=max_element(exp.begin(),exp.end())-exp.begin();
            wallet = 0;

            for (int i=0; i<max_idx; ++i) {
                wallet += exp.front();
                exp.pop_front();
            }

            revenue += max_idx*exp.front() - wallet;
            exp.pop_front();

            if (exp.empty()) break;

        }
        cout<<"#"<<test_case<<" "<<revenue<<"\n";
	}

    
	return 0;
}