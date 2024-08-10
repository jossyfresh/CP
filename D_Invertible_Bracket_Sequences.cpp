// D //
#include <iostream>
#include <string>
#include <vector>
using namespace std;

// Function to count the number of valid pairs (l, r) where replacing the substring with its inverse keeps the sequence regular
int countValidPairs(const string& s) {
    int n = s.length();
    int balance = 0;
    int validPairs = 0;

    // Using a vector to keep track of balance values
    vector<int> balanceCount(2 * n + 1, 0);
    balanceCount[n] = 1; // Initial balance (0 balance at position n)

    for (char c : s) {
        if (c == '(') {
            balance++;
        } else {
            balance--;
        }
        validPairs += balanceCount[balance + n];
        balanceCount[balance + n]++;
    }

    return validPairs;
}

int main() {
    int t;
    cin >> t;
    while (t--) {
        string s;
        cin >> s;
        cout << countValidPairs(s) << endl;
    }
    return 0;
}