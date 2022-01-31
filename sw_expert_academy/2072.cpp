#include <iostream>
#include <vector>

using namespace std;

int main() {
    int input_count;
    int **arr;

    cin >> input_count;
    arr = new int*[input_count];
    vector<int> result(input_count);
    for (int i=0; i<input_count; i++) {
        arr[i] = new int[10];
    }

    for (int i=0; i<input_count; i++) {
        for (int j=0; j<10; j++) {
        cin >> arr[i][j];
        }
    }

    for (int i=0; i<input_count; i++) {
        for (int j=0; j<10; j++) {
            if ((arr[i][j] % 2) != 0) result[i] = result[i]+arr[i][j];
        }
    }

    for (int i=0; i<input_count; i++) {
        cout<<"#"<<i+1<<" "<<result[i]<<"\n";
    }

    delete[] arr;

}