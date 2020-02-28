#include<iostream>
#include<algorithm>
using namespace std;
int main(){
        int a,b,c;
        cin >> a >> b >> c;
        int sum = max(max(a,b),c)*10;
                if(sum/10==a) sum+=b+c; 
                if(sum/10==b) sum+=a+c;
                if(sum/10==c) sum+=a+b;
        cout << sum << endl;
}
