#include <bits/stdc++.h>
using namespace std;
vector<string> split(string s){
    vector<string> v;
    string temp = "";
    for (int i = 0; i < s.length(); i++){
        if (s[i] == ' '){
            v.push_back(temp);
            temp = "";
        }
        else{
            temp += s[i];
        }
    }
    v.push_back(temp);
    return v;
}
void solve(){
    int n;
    int ans = 0;
    cin >> n;
    vector<int>temp(0);
    string s;
    int time = 1;
    for (int i = 0; i < n; i++){
        cin >> s;
        vector<string> cmd = split(s);
        cout<<cmd[0]<<endl;
        if (cmd[0] == "add"){
            ans  += time;
        }
        else if (cmd[0] == "for"){
            temp.push_back(stoi(cmd[1]));
            time *= stoi(cmd[1]);
        }
        else if(cmd[0] == "end"){
            time = int(time/temp.back());
            temp.pop_back();
        }
    cout<<ans<<endl;
    }  
}
int main(){
    solve();
    return 0;
}