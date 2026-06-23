from collections import deque

class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        MOD = 10**9 + 7
        
        n = 0
        for u, v in edges:
            n = max(n, u, v)
            
        adj = [[] for _ in range(n + 1)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        max_depth = 0
        q = deque([(1, 0)])
        visited = {1}
        
        while q:
            node, dist = q.popleft()
            max_depth = max(max_depth, dist)
            for neighbor in adj[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    q.append((neighbor, dist + 1))
                    
        if max_depth == 0:
            return 0
            
        return pow(2, max_depth - 1, MOD)
