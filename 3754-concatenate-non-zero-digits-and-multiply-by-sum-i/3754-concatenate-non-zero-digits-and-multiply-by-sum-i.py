class Solution:
    def sumAndMultiply(self, n: int) -> int:
        non_zero_digits = [char for char in str(n) if char != '0']
        
        if not non_zero_digits:
            return 0
        
        x_str = "".join(non_zero_digits)
        x = int(x_str)
        digit_sum = sum(int(char) for char in x_str)
        
        return x * digit_sum
