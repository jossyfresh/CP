#include <iostream> 
#include <vector> 
#include <set> 
#include <algorithm>
using namespace std;
void solveTestCase() {
    int n; 
    cin >> n;
    vector<int> a(n);
    set<int> distinctValues;
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
        cout << a[i] << ' ';
        distinctValues.insert(a[i]);
    }
    vector<int> distinctVec(distinctValues.begin(),distinctValues.end());
    if (distinctVec.size() == 1) { 
        cout << 0 << endl;
         return;
    }
   
    if (distinctVec.size() == 2) { 
        cout << 1 << endl;
        cout << distinctVec[1] << endl;
        return;
    }
    
    if (distinctVec.size() == 3) {
        cout << 2 << endl;
        cout << distinctVec[2] << ' ' << distinctVec[1] << endl;
        return;
    }
    cout << -1 << endl;
}
int main() {
    int t; 
    cin >> t;
    while (t--) {
        solveTestCase();
    }
    return 0;
}