#include <bits/stdc++.h>

using namespace std;
typedef long long int ll;

struct wrb
{
    int w;
    int b;
    int r;
};

int main()
{
    int n, m;
    bool w = true, b = false, r = false;
    cin >> n >> m;
    vector<string> mas(n);
    for (int i = 0; i < n; i++)
    {
        cin >> mas[i];
    }
    wrb count[n + 1] = {};
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            if (mas[i][j] == 'W')
            {
                count[i + 1].b++;
                count[i + 1].r++;
            }
            else if (mas[i][j] == 'B')
            {
                count[i + 1].w++;
                count[i + 1].r++;
            }
            else if (mas[i][j] == 'R')
            {
                count[i + 1].w++;
                count[i + 1].b++;
            }
        }
    }
    int ret = n * m;

    for (int i = 0; i < n; i++)
    {
        count[i + 1].w += count[i].w;
        count[i + 1].r += count[i].r;
        count[i + 1].b += count[i].b;
    }
    for (int w = 1; w < n - 1; w++)
    {
        for (int b = w + 1; b < n; b++)
        {
            ret = min(ret, count[w].w + count[b].b - count[w].b + count[n].r - count[b].r);
            // cout << ret << endl;
        }
    }
    cout << ret << endl;
}