class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        res = []
        
        def backtrack(index, path, eval_val, prev_val):
            # Base Case: Agar poori string process ho gayi
            if index == len(num):
                if eval_val == target:
                    res.append(path)
                return
            
            # String ke bache hue hisse ke different lengths explore karo
            for j in range(index, len(num)):
                # Leading Zero Check: "0" ke baad "05" jaisa number valid nahi hai
                if j > index and num[index] == '0':
                    break
                    
                sub_str = num[index : j + 1]
                curr_num = int(sub_str)
                
                # Agar pehla number hai (expression shuru ho raha hai)
                if index == 0:
                    backtrack(j + 1, sub_str, curr_num, curr_num)
                else:
                    # Choice 1: Addition '+'
                    backtrack(j + 1, path + '+' + sub_str, eval_val + curr_num, curr_num)
                    
                    # Choice 2: Subtraction '-'
                    backtrack(j + 1, path + '-' + sub_str, eval_val - curr_num, -curr_num)
                    
                    # Choice 3: Multiplication '*'
                    backtrack(j + 1, path + '*' + sub_str, eval_val - prev_val + (prev_val * curr_num), prev_val * curr_num)
                    
        backtrack(0, "", 0, 0)
        return res