#include<iostream>
#include<cstdio>
using namespace std;
int main(){
    int x1,x2,y1,y2,xmar,ymar;
    int x3,y3,x4,y4;
    scanf("%d %d %d %d",&x1,&y1,&x2,&y2);
    xmar = x2-x1; ymar = y2-y1;
    x3 = x2-ymar; y3 = y2+xmar;
    x4 = x3-xmar; y4 = y3-ymar;
    printf("%d %d %d %d\n",x3,y3,x4,y4);
}
