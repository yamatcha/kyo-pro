#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
    int n, m, l, tmp;
    cin >> n >> m;
    vector<int> a;
    for (int i = 0; i < n; i++)
    {
        cin >> l;
        a.push_back(l);
    }
    for (int k = 1; k < m + 1; k++)
    {
        for (int i = 0; i < n - 1; i++)
        {
            if (a[i] % k > a[i + 1] % k)
            {
                swap(a[i], a[i + 1]);
            }
        }
    }
    for (int i = 0; i < n; i++)
    {
        cout << a[i] << endl;
    }
}