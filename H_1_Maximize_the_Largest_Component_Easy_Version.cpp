#include <iostream>

using namespace std;

int main() {
    int t;
    cin >> t;

    while (t--) {
        int n, x;
        cin >> n >> x;
        long long count = 0;
        for (int a = 1; a <= x; ++a) {
            int b_max = min(x - a, n / a);
            for (int b = 1; b <= b_max; ++b) {
                int c_max = min(x - a - b, (n - a * b) / (a + b));
                count += max(0, c_max);
            }
        }
        cout << count << "\n";
    }
    return 0;
}
