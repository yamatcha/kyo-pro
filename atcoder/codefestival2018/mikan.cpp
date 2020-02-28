#include<iostream>
#include<vector>
using namespace std;
int main(){
        int n,m,a,b,i,j,cl,cr;
        int max = 0;
        int sum=0;
        vector<int> l,r;
        cin >> n >> m >> a >> b;
        while(cin>>cl){
                l.push_back(cl);
                cin>>cr;
                r.push_back(cr);
                if(r[r.size()-1]>max) max = r[r.size()-1];
        }
        int ar[n+1];
        for(i=0;i<n+1;i++) ar[i] = 0;
        for(i=0;i<l.size();i++)
                for(j=l[i];j<=r[i];j++){
                        if(ar[j]!=1) ar[j]=1;
                }
        for(i=1;i<=n;i++){
                if(ar[i]==1) sum+=a;
                else sum+=b;
        }
        cout<<sum<<endl;
}

                
