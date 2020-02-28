#include<iostream>
using namespace std;
int main(){
        int i,odd,even;
        cin >> i;
        odd = i/2;
        even = i/2;
        if(i%2==1) odd++;
        cout << odd*even <<endl;
}
