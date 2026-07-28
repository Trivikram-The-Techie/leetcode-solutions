class Solution:
    def smallestPalindrome(self, s: str) -> str:
        n = len(s)
        half_len = n // 2
        
        # Sort the first half to get the smallest lexicographical order
        first_half = "".join(sorted(s[:half_len]))
        
        # If length is odd, keep the middle character
        mid = s[half_len] if n % 2 != 0 else ""
        
        # Combine first half, middle character, and the reversed first half
        return first_half + mid + first_half[::-1]