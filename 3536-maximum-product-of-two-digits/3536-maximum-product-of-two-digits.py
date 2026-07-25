class Solution:
    def maxProduct(self, n: int) -> int:
        # Convert integer to string to get digits, then sort them
        digits = sorted([int(d) for d in str(n)])
        
        # The maximum product comes from the two largest digits
        return digits[-1] * digits[-2]