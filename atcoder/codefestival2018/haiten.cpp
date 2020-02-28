#include<iostream>
using namespace std;
int main(){
        int a,b,c,s;
        int jud = 0;
        cin >>a >> b >> c >>s;
        if(a+b+c+3>=s && a+b+c<=s)
                cout << "Yes"<<endl;
        else cout << "No"<<endl;
}
        
