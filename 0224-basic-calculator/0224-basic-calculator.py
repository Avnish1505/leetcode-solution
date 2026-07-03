class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        result = 0
        num = 0
        sign = 1  # 1 matlab positive (+), -1 matlab negative (-)
        
        for char in s:
            if char.isdigit():
                # Handling multi-digit numbers (e.g., "123")
                num = num * 10 + int(char)
                
            elif char == '+':
                # Pichle number ko evaluate karke result mein daalo
                result += sign * num
                # Sign update karo aur number ko reset
                sign = 1
                num = 0
                
            elif char == '-':
                # Same process as plus
                result += sign * num
                sign = -1
                num = 0
                
            elif char == '(':
                # Current state ko stack mein push karo
                # [pichla_result, pichla_sign]
                stack.append(result)
                stack.append(sign)
                # Naye bracket ke liye state reset karo
                result = 0
                sign = 1
                
            elif char == ')':
                # Bracket ke andar ka bacha hua number add karo
                result += sign * num
                num = 0
                
                # Stack se pehle pichla sign pop karo, fir multiply karo
                prev_sign = stack.pop()
                result *= prev_sign
                
                # Stack se pichla result pop karo aur add karo
                prev_result = stack.pop()
                result += prev_result
                
        # Loop khatam hone par agar koi aakhri number bacha hai, toh add karo
        result += sign * num
        return result