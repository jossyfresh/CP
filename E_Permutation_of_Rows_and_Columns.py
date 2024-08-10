#include <iostream>
#include<bits/stdc++.h>
#define int long long
using namespace std;




void sol(){
 
 
 int n;
 cin>>n;
 vector<int> v(n);
 
 for(auto &val:v) cin>>val;
 
 int x = 1;
 
 for(auto &val:v){
   int y = __gcd(x,val);
   y = val/y;
   x*=y;
 }
 int sum = 0;
 vector<int> ans;
 for(auto &val:v){
   sum+=x/val;
   ans.push_back(x/val);
 }
 
 if(sum>=x){
   cout<<-1<<endl;
 }
 else{
   for(auto &val:ans){
     cout<<val<<" ";
   }
   cout<<endl;
 }
 
  return;
}

signed main() 
{
  int test;
  cin>>test;
  while(test--){
    sol();
  }
   
    return 0;
}