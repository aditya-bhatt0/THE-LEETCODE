class Solution:
    def myAtoi(self, s: str) -> int:
        n = len(s)
        i = 0
        result = 0
        sign = 1
        
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1
        
        while i < n and s[i].isspace():
            i += 1
            
        if i < n:
            if s[i] == '-':
                sign = -1
                i += 1
            elif s[i] == '+':
                i += 1
                
        while i < n and s[i].isdigit():
            result = result * 10 + int(s[i])
            i += 1
            
        result *= sign
        
        if result < INT_MIN:
            return INT_MIN
        if result > INT_MAX:
            return INT_MAX
            
        return result
