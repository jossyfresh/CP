#include <iostream>
#include<bits/stdc++.h>
using namespace std;

#define int long long

signed main() 
{
    int t;
    cin>>t;
    while(t--){
      
     int n;
     cin>>n;
     
     vector<int> a(n),b(n);
     
     for(auto &val:a) cin>>val;
     for(auto &val:b) cin>>val;
     
     int count = 0,P = 0,N = 0;
     
    for(int i = 0;i<n;i++){
      if(a[i]==b[i]){
        if(a[i]==-1){
          N--;
        }
        else if(a[i]==1){
            P++;
        }
      }
    }
      
      
      int A = 0,B = 0;
      
      for(auto i = 0;i<n;i++){
        
        if(a[i]==b[i]) continue;
        
        if(a[i]>b[i]){
          A+=a[i];
        }
        else{
          B+=b[i];
        }
        
      }
      
      
      if(A>B) swap(A,B);
      
      count = P;
        int x = min(B-A,count);
        A+=x;
        count-=x;
        x = count/2;
        count = count - x;
        A+=max(x,count);
        B+=min(x,count);
      if(A>B) swap(A,B);
      count = N;
        x = max(A-B,count);
        B+=x;
        count-=x;
        x = count/2;
        count = count - x;
        A+=max(x,count);
        B+=min(x,count);
      
      
      
      cout<<min(A,B)<<endl;
      
    }
   
    
    return 0;
}
