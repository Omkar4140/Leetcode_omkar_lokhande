class Solution:
    def shortestPathLength(self, graph: list[list[int]]) -> int:
        n =len(graph)
        final_mask = (1 << n) - 1

        queue = deque([i, 1 << i, 0]for i in range(n))
        visited = set((i,i << i)for i in range(n))

        while queue:
            node,mask,steps = queue.popleft()

            if mask == final_mask:
                return steps
            
            for neighbor in graph[node]:
                new_mask = mask | (1 << neighbor)

                if (neighbor, new_mask) not in visited:
                    visited.add((neighbor , new_mask))
                    queue.append ([neighbor, new_mask, steps +1])
        return -1

        