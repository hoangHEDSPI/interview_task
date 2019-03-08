/*
Problem set : https://www.hackerrank.com/challenges/angry-children/problem
*/

#include <bits/stdc++.h>

using namespace std;

// Complete the maxMin function below.
int maxMin(int k, vector<int> arr) {
    std::sort(arr.begin(), arr.end());
    int res = arr[arr.size()-1];
    for (int i = 0; i < arr.size()-k+1; i++) {
        if (res > arr[i+k-1] - arr[i]) {
            res = arr[i+k-1] - arr[i];
        }
        cout << "arr[i+k-1] = " << arr[i+k-1] << endl;
    }
    return res;

}

int main()
{
    // ofstream fout(getenv("OUTPUT_PATH"));

    int n;
    cin >> n;
    // cin.ignore(numeric_limits<streamsize>::max(), '\n');

    int k;
    cin >> k;
    // cin.ignore(numeric_limits<streamsize>::max(), '\n');

    vector<int> arr(n);

    for (int i = 0; i < n; i++) {
        int arr_item;
        cin >> arr_item;
        // cin.ignore(numeric_limits<streamsize>::max(), '\n');

        arr[i] = arr_item;
    }

    int result = maxMin(k, arr);

    cout << result << "\n";

    // fout.close();

    return 0;
}