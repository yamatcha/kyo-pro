#include<iostream>
#include<algorithm>
using namespace std;
int main(){
        int n,m,x,y,i;
        int ma = 0;
        int mi = 101;
        cin >> n >> m >> x >>y;
        int xc[n];
        int yc[m];
        for(i=0;i<n;i++){
                cin >> xc[i];
                ma = max(ma,xc[i]);
        }
        for(i=0;i<m;i++){
                cin >> yc[i];
                mi = min(mi,yc[i]);
        }
        if(mi>ma && x<ma && y>=ma) cout <<"No war" << endl;
        else cout << "War" << endl;
}

