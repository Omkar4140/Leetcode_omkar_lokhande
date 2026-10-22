class Solution:
    def isBipartite(self, graph: list[list[int]]) -> bool:
        color = [-1] * len(graph)

        for i in range (len(graph)):
            if color[i] != -1:
                continue
            color[i]=0
            q=deque([i])
            while q:
                u= q.popleft()
                for v in graph[u]:
                    if color[v] == -1:
                        color[v] = 1 - color[u]
                        q.append(v)
                    elif color[v] ==color[u]:
                        return False
        return True