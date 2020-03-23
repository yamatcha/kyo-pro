#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
    vector<int> a(4), b(2);
    int l;
    for (int i = 0; i < 6; i++)
    {
        cin >> l;
        if (i < 4)
        {
            a.push_back(l);
        }
        else
        {
            b.push_back(l);
        }
    }

    sort(a.begin(), a.end());
    sort(b.begin(), b.end());
    reverse(a.begin(), a.end());
    reverse(b.begin(), b.end());
    // cout << a[0] << b[0];
    cout << a[0] + a[1] + a[2] + b[0] << endl;
}