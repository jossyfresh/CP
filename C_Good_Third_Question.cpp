#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int main()
{
    int n,m;
    cin >> n >> m;
    vector<int> num(n);
    for(int i = 0; i < n; i++)
        cin >> num[i];
    sort(num.begin(), num.end());
    for(int i = 0; i < n; i++)
    {
        int x;
        cin >> x;
        int b = lower_bound(num.begin(), num.end(), x);
        cout << b << endl;
        int l = num.size() - b;
        if(l < num.size() && l >= num.size()/2 + 1)
            cout << "YES" << endl;
        else
            cout << "NO" << endl;
    }
    return 0;
}