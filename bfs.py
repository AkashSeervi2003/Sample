graph = {
    5 : [3,7],
    3 : [2,4],
    7 : [8],
    2 : [],
    4 : [8],
    8 : []
}
visited = []
queue = []
def bfs(visited,graph,node):
    visited.append(node)
    queue.append(node)
    while queue:
        m = queue.pop(0)
        print(m, end=" ")
        for i in graph[m]:
            visited.append(i)
            queue.append(i)
print("Following is the Breadth First Search")
bfs(visited,graph,5)