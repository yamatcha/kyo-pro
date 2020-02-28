#include<iostream>
using namespace std;
int main(){
        int n,k,i,j,l;
        l=0;
        int a[1000000];
        int cnt = 0;
        cin >> n >> k;
        for(i=1;i<=n;i++){
                        if((2*i)%k==0 ){
                                cnt++;
                                a[l] = i;
                                l++;
                                }
        }
        for(i=0;i+1<l;i++){
                for(j=i+1;j<l;j++){
                        if((a[i]+a[j])%k==0){
                                cnt+=6;
                        }
                }
        }
        cout << cnt<<endl;
}
