from collections import defaultdict, deque
from typing import List

class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        # Step 1: Build the directed graph (adjacency list)
        graph = defaultdict(list)
        for u, v in invocations:
            graph[u].append(v)
            
        # Step 2: Find all suspicious methods using BFS starting from k
        suspicious = set([k])
        queue = deque([k])
        
        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                if neighbor not in suspicious:
                    suspicious.add(neighbor)
                    queue.append(neighbor)
                    
        # Step 3: Check if any non-suspicious method invokes a suspicious method
        for u, v in invocations:
            if u not in suspicious and v in suspicious:
                # Cannot remove suspicious methods; return all methods
                return list(range(n))
                
        # Step 4: Return all remaining (non-suspicious) methods
        return [i for i in range(n) if i not in suspicious]