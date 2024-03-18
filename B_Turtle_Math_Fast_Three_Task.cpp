#include<bits/stdc++.h>
using namespace std;
#define ll long long
#define ld long double
#define inf std::numeric_limits<int>::max();
#define mod 10000000007
#define yup cout<<"YES"<<endl;
#define nope cout<<"NO"<<endl;

void solutioN()
{
    ll n; cin>> n;
    vector<ll> v(n);
    set<ll> st;
    ll total = 0;

    for(int i=0; i<n; i++)
    {
        cin>> v[i];
        st.insert(v[i]);
        total += v[i];
    }

    if(total%3==0)
    {
        cout<< "0" <<endl;
        return;
    }
    else if((total+1)%3==0)
    {
        cout<< "1" <<endl;
        return;
    }
    else
    {
        ll kk = 1;
        ll mx = *max_element(v.begin(),v.end());
        while (kk <= mx)
        {
            if(st.find(kk) != st.end())
            {
                cout<< "1" <<endl;
                return;
            }
            kk+=3;
        }

        cout<< "2" <<endl;
        return;
    }
}

void solve_mul()
{ ll test; cin>>test; while (test--) {solutioN();} }

void solve_single(){solutioN();}

int main()
{
    ios_base::sync_with_stdio(false);
    solve_mul();
    //solve_single();
}






/*                                Ⓒ All rights reserved to Prnc                              */
