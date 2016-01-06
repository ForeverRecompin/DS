#include <bits/stdc++.h>
using namespace std;

typedef pair<int, int> II;
typedef vector<int> VI;
typedef vector<II> VII;

#define VISITED 1
#define UNVISITED 0

VI dfs_num;
vector<VII> AdjList;

void dfs(int u){
  dfs_num[u] = VISITED;
  cout << u << " "; 
  for (int i = 0; i < (int)AdjList[u].size(); i++){
    II v = AdjList[u][i];
    if (dfs_num[v.first] == UNVISITED){
      dfs(v.first);
    }
  }
}

int main(int argc, char** argv){
  int V, E, total_neighbors, id, weight;
  cout << "\nNo of vertices = ";
  cin >> V;
  dfs_num.assign(V, UNVISITED);
  AdjList.assign(V, VII());
  for(int i = 0; i < V; i++){
    cin >> total_neighbors;
    for(int j = 0; j < total_neighbors; j++){
      cin >> id >> weight;
      AdjList[i].push_back(II(id, weight));
    }
  }
  dfs(0);
  return 0;
}
