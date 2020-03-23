#include <bits/stdc++.h>
using namespace std;

vector<pair<int, int>> fri, blo;
vector<int> Group;
vector<vector<int>> G(100001);

void dfs(int now, int parent)
{
    Group[now] = parent;
    for (int &x : G[now])
    {
        if (Group[x] == -1)
        {
            dfs(x, parent);
        }
    }
}

int main()
{
    int n, m, k;
    cin >> n >> m >> k;
    blo.resize(k);
    fri.resize(m);
    Group.resize(n, -1);
    for (int i = 0; i < m; i++)
    {
        int a, b;
        cin >> a >> b;
        G[--a].push_back(--b);
        G[b].push_back(a);
        fri[i] = {a, b};
    }

    for (int i = 0; i < k; i++)
    {
        int a, b;
        cin >> a >> b;
        blo[i] = {--a, --b};
    }
    for (int i = 0; i < n; i++)
    {
        if (Group[i] == -1)
            dfs(i, i);
    }
    vector<int> cnt(n, 0);
    for (int &x : Group)
    {
        cnt[x]++;
    }
    vector<int> ret(n, 0);
    for (int i = 0; i < n; i++)
    {
        ret[i] = cnt[Group[i]] - 1;
    }
    for (auto &x : fri)
    {
        ret[x.first]--;
        ret[x.second]--;
    }
    for (auto &x : blo)
    {
        if (Group[x.first] == Group[x.second])
        {
            ret[x.first]--;
            ret[x.second]--;
        }
    }
    for (auto &x : ret)
    {
        cout << x << " ";
    }
    cout << endl;
    return 0;
}