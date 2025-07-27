#include <bits/stdc++.h>
using namespace std;
void bfs(int i,int j,vector<vector<int>>grid,vector<vector<bool>>&visited){
    visited[i][j] = true;
    queue<pair<int,int>>q;
    q.push({i,j});
    int dx[4] = {0,0,1,-1};
    int dy[4] = {1,-1,0,0};
    while(!q.empty()){
        auto p = q.front();
        q.pop();
        int x = p.first;
        int y = p.second;
        visited[x][y] = true;
        for(int i=0;i<4;i++){
            int newx = x+dx[i];
            int newy = y+dy[i];
            if(newx<grid.size()&&newy<grid[0].size()&&newx>=0&&newy>=0&&!visited[newx][newy]&&grid[newx][newy]==1){
                q.push({newx,newy});
            }
        }
    }
}
int main() {
    int n,m;
    cin>>n>>m;
    vector<vector<int>>matrix(n,vector<int>(m));
    for(int i=0;i<n;i++){
        for(int j=0;j<m;j++){
            cin>>matrix[i][j];
        }
    }
    //bfs solution 
    vector<vector<bool>>visited(n,vector<bool>(m,false));
    int ans =0;
    for(int i=0;i<n;i++){
        for(int j=0;j<m;j++){
            if(matrix[i][j]==1&&!visited[i][j]){
                bfs(i,j,matrix,visited);
                ans++;
            }
        }
    }
    cout<<ans<<endl;
}
