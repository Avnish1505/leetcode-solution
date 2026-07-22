class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 1. Adjacency List banao: course -> list of prerequisites/dependents
        adj = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            adj[crs].append(pre)
            
        # 0 = Unvisited, 1 = Visiting (current stack), 2 = Visited
        state = [0] * numCourses
        
        def dfs(crs):
            # Agar current recursion stack mein dobara wapas aaye -> Cycle Found!
            if state[crs] == 1:
                return False
            # Agar pehle se poora explore ho chuka hai -> No Cycle here
            if state[crs] == 2:
                return True
                
            # Current node ko 'Visiting' mark karo
            state[crs] = 1
            
            # Iske saare prerequisites ko check karo
            for pre in adj[crs]:
                if not dfs(pre):
                    return False
                    
            # Fully explore hone ke baad 'Visited' mark karo
            state[crs] = 2
            return True

        # Saare courses ke liye check karo (kyunki graph disconnected bhi ho sakta hai)
        for i in range(numCourses):
            if not dfs(i):
                return False
                
        return True