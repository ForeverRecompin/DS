#include <bits/stdc++.h>
using namespace std;

typedef pair<int, int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;

#define V 3
#define INF 1000000000

vector<vii> AdjList; 
vi d(V,INF);

void bfs(int s)
{
  queue<int> q;
  q.push(s);

  while(!q.empty())
  {
    int u = q.front();
    q.pop();
    cout << u << " ";
    for(int i=0; i<(int)AdjList[u].size(); i++)
    {
      ii v = AdjList[u][i];
      if(d[v.first] == INF)
      {
        d[v.first] = d[u] + 1;
        q.push(v.first);
      }
    }
  }
}

int main(int argc, char* argv[])
{
  int num_neighbors, id, wt;
  AdjList.assign(V,vii());
  for(int i=0; i<V; i++)
  {
    cin >> num_neighbors;
    cout << num_neighbors << " of " << i << endl; 
    for(int j=0; j<num_neighbors; j++)
    {
      cin >> id >> wt;
      cout << id << " " << wt << endl;
      cout << "LOLOLOL" << endl;
      AdjList[i].push_back(ii(id,wt));
    }
  }
  bfs(0);
  return 0;
}
