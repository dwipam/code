class cgraph(object):
    def __init__(self,n,m,graph):
        self.n = n
        self.m = m
        self.graph = graph
        self.visited = [[False for j in i] for i in graph]
    def is_safe(self,i,j):
        return(i>=0 and i<self.n and \
                j>=0 and j<self.m and \
                self.graph[i][j] and not self.visited[i][j])
    def dfs(self,i,j):
        row = [-1,-1,-1,0,0,1,1,1]
        col = [1,-1,0,-1,1,-1,1,0]
        self.visited[i][j] = True
        for k in range(8):
            if self.is_safe(i+row[k],j+col[k]):
                self.dfs(i+row[k],j+col[k])
    def countIsland(self):
        count = 0
        for i in range(self.n):
            for j in range(self.m):
                if self.is_safe(i,j):
                    self.dfs(i,j)
                    count+=1
        return count

g = [[1,1,1,0],[0,0,0,1],[0,0,0,0],[1,0,1,0]]
getgraph = cgraph(len(g),len(g[0]),g)
print(getgraph.countIsland())

        

