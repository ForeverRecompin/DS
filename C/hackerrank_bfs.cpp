#include <bits/stdc++.h>
using namespace std;

typedef pair<int,int> ii;
typedef vector<ii> vii;
typedef vector<int> vi;

#define INF 1000000000
#define NIL -1

int main(int argc, char *argv[])
{
  int tc;
  cin >> tc;
  while (tc--) {

    // ---- Initialization ----
    int N, M, x, y, s; // N = #(Vertices), M = #(Edges), x-->y = Edge, s = Starting vertex.
    cin >> N >> M; // N -> [1,N].

    // ---- Input the Adjacency List ----
    vector<vii> AdjList;
    AdjList.assign(N, vii());
    for (int i = 0; i < M; i++) {
      cin >> x >> y;
      AdjList[x-1].push_back(ii(y-1,0));
      AdjList[y-1].push_back(ii(x-1,0));
    }
    cin >> s;
    s--; 

    // ---- BFS ----
    vi dist(N, INF);
    vi p; 
    dist[s] = 0;
    p.assign(N, NIL);
    queue<int> q;
    q.push(s);

    while (!q.empty()) {
      int u = q.front();
      q.pop();
      for (int i = 0; i < int(AdjList[u].size()); i++) {
        ii v = AdjList[u][i];
        if (dist[v.first] == INF) {
          dist[v.first] = dist[u] + 1;
          p[v.first] = u;
          q.push(v.first);
        }
      }
    }

    for (int i = 0; i < N; i++) {
      if (i == s) continue;
      if (dist[i] != INF) {
        cout << ((dist[i])*6) << " ";
      }
      else {
        cout << -1 << " ";
      }
    }
    cout << endl;
  }

  return 0;
}
