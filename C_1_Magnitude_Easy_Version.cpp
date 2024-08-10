#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int maxErrorsInWindow(const vector<int>& error_count, int K) {
    int N = error_count.size();
    if (N < K) return -1; // If the array is smaller than the window size, it's not possible

    // Calculate the sum of the first window of size K
    int current_sum = 0;
    for (int i = 0; i < K; i++) {
        current_sum += error_count[i];
    }

    int max_sum = current_sum;

    // Slide the window from start to end of the array
    for (int i = K; i < N; i++) {
        current_sum += error_count[i] - error_count[i - K];
        max_sum = max(max_sum, current_sum);
    }

    return max_sum;
}

int main() {
    int N, K;
    
    // Input the size of the error logs list
    cin >> N;
    
    vector<int> error_count(N);
    
    // Input the error counts for each second
    for (int i = 0; i < N; i++) {
        cin >> error_count[i];
    }
    
    // Input the window size K
    cin >> K;
    
    // Calculate and print the maximum number of errors in any K-second window
    cout << maxErrorsInWindow(error_count, K) << endl;

    return 0;
}