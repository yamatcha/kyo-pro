#include<iostream>
#include<vector>
using namespace std;

int cnt[10000];

int vec_find(std::vector<int> vec, int number){
 auto itr = std::find(vec.begin(), vec.end(), number);
 size_t index = std::distance( vec.begin(), itr );
  if (index != vec.size()) { // 発見できたとき
    return 1;
  }
  else { // 発見できなかったとき
   return 0;
  }
}

void recog(int x,int jud,vector<int> i){
                if(vec_find(i,x)) cnt[x]++;
                else i.push_back(x);
}

int main(){
        int n,i;
        int maxa=0,maxb=0;
        cin >> n;
        int m[n];
        vector<int> a;
        vector<int> b;
        for(i=0;i<n;i++)
                cin >> m[i];

        for(i=0;i<n;i+=2)
                recog(m[i],0,a);
        for(i=1;i<n;i+=2)
                recog(m[i],1,b);
                cout << a.size<<endl;
        for(i=0;i<n;i+=2){
                if(maxa<a.at(i)) maxa = a.at(m[i]);
        }
        for(i=1;i<n;i+=2){
                if(maxb<b.at(i)) maxb = b.at(m[i]);
        }
        cout << (n-maxa-maxb) << endl;
        return 0;
}
