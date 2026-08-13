class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        min_x = float('inf')
        min_y = float('inf')
        max_x = float('-inf')
        max_y = float('-inf')
        
        total_area = 0
        corners = set()
        
        for x1, y1, x2, y2 in rectangles:
            # Bounding box bounds update karo
            min_x = min(min_x, x1)
            min_y = min(min_y, y1)
            max_x = max(max_x, x2)
            max_y = max(max_y, y2)
            
            # Individual rectangle area calculate karke sum karo
            total_area += (x2 - x1) * (y2 - y1)
            
            # Current rectangle ke 4 corners
            p1 = (x1, y1)
            p2 = (x1, y2)
            p3 = (x2, y1)
            p4 = (x2, y2)
            
            # Corners ko toggle karo set ke andar
            for p in (p1, p2, p3, p4):
                if p in corners:
                    corners.remove(p)
                else:
                    corners.add(p)
                    
        # Condition 1: Total area bounding area ke equal hona chahiye
        expected_area = (max_x - min_x) * (max_y - min_y)
        if total_area != expected_area:
            return False
            
        # Condition 2: Corner set mein exact 4 points hone chahiye aur wo bounding corners hone chahiye
        expected_corners = {
            (min_x, min_y),
            (min_x, max_y),
            (max_x, min_y),
            (max_x, max_y)
        }
        
        return corners == expected_corners