class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        # Step 1: list1 ke elements ko unke index ke saath dictionary mein daalo
        val_to_index = {val: i for i, val in enumerate(list1)}
        
        min_sum = float('inf')
        result = []
        
        # Step 2: list2 par iterate karke common strings dhoondho
        for j, val in enumerate(list2):
            if val in val_to_index:
                i = val_to_index[val]
                current_sum = i + j
                
                # Agar naya index sum chota hai
                if current_sum < min_sum:
                    min_sum = current_sum
                    result = [val]  # Purana result hatao, naya start karo
                # Agar index sum barabar hai, toh result mein add kar lo
                elif current_sum == min_sum:
                    result.append(val)
                    
        return result