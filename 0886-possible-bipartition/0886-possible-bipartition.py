class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        # 1. Graph (Adjacency List) banana
        graph = defaultdict(list)
        for u, v in dislikes:
            graph[u].append(v)
            graph[v].append(u)
            
        # 2. Color map: -1 matlab uncolored, 0 aur 1 do alag groups hain
        color = {}
        
        # 3. Saare logo ke liye check karo (kuch log disconnected bhi ho sakte hain)
        for i in range(1, n + 1):
            if i not in color:
                # BFS shuru karo ek naye component ke liye
                queue = deque([i])
                color[i] = 0  # Pehle bande ko group 0 de diya
                
                while queue:
                    curr = queue.popleft()
                    
                    for neighbor in graph[curr]:
                        # Agar dushman ko abhi tak group nahi mila
                        if neighbor not in color:
                            # Use opposite group mein daalo
                            color[neighbor] = 1 - color[curr]
                            queue.append(neighbor)
                        # Agar dushman pehle se same group mein baitha hai!
                        elif color[neighbor] == color[curr]:
                            return False
                            
        return True