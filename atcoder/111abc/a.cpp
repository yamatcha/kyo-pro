#include<iostream>
using namespace std;
int main(){
        int n,i;
        int a[3];
        cin >> n;
        a[0] = n%10;
        a[1] = n/10%10;
        a[2] = n/100;
        for(i=0;i<3;i++){
                if(a[i]==1) a[i]=9;
                else a[i] = 1;
        }
        cout << a[2]*100+a[1]*10+a[0] << endl;
}
