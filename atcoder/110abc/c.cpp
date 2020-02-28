#include<iostream>
#include<vector>
using namespace std;
int main(){
        string s,t;
        char cs,ct;
        vector<char> van;
        cin >> s >> t;
        int i,j,jud;
        for(i=0;i<s.length();i++){
                jud = 1;
                for(j=0;j<van.size();j++)
                        if(van.at(j) == i){ jud = 0;
                        }
                if(s[i]!=t[i] && jud){
                        cs = s[i]; ct = t[i];
                        for(j=0;j<s.length();j++){
                                if(s[j]==cs){
                                        s[j] = ct;
                                         van.push_back(j);
                                         continue;
                                }
                                if(s[j]==ct){
                                        s[j]=cs;
                                        van.push_back(j);
                                }
                        }
                        }
                }
        if(s==t) cout << "Yes" <<endl;
        else cout << "No" << endl;
        cout << t<<endl;
        cout << s<<endl;
}
