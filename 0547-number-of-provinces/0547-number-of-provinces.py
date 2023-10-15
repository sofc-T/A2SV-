class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def DFS(visited,graph,source):
            visited[source] = True
            for i in graph[source]:
                if visited[i] == False:
                    DFS(visited,graph,i)
        graph = [[] for i in range(len(isConnected)+1)]
        for i in range(len(isConnected)):
            for j in range(len(isConnected)):
                if i!=j and isConnected[i][j] == 1:
                    graph[i+1].append(j+1)
        visited = [False for i in range(len(isConnected)+1)]
        count = 0
        for i in range(1,len(visited)):
            if visited[i] == False:
                DFS(visited,graph,i)
                count+=1
        return count