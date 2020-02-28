#include<iostream>
using namespace std;
int main(){
        int n,i,j;
        cin >> n;
        int a[3];
        a[0] = n%10;
        a[1] = n/10%10;
        a[2] = n/100;
        for(i=a[2]-1;i<10;i++){
                j = i+1;
                if((n<=(j*100+j*10+j))&&(n>(i*100+i*10+i))){
                         break;
                }
        }
        cout << j * 100 + j *10 + j << endl;
}
