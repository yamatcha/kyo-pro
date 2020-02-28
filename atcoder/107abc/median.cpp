#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;
int main(){
        int n;
        cin >> n;
        vector<int> vc;
        if(n==1){
                int x;
                cin>>x; 
                cout << x << endl;
        }else{ 
        while(n--){
                int x;
                cin>>x;
                vc.push_back(x);
        }
                sort(vc.begin(),vc.end());
                cout << vc[vc.size()/2+1] << endl;
        }
}

