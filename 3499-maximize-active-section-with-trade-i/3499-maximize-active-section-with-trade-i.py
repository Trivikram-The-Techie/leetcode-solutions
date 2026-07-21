class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        # Calculate initial count of '1's
        total_ones = s.count('1')
        
        # Extract the lengths of all contiguous '0' blocks
        zero_blocks = [len(block) for block in s.split('1') if block]
        
        # If there are at least two zero blocks, find the max sum of adjacent zero blocks
        max_gain = 0
        if len(zero_blocks) >= 2:
            max_gain = max(a + b for a, b in zip(zero_blocks, zero_blocks[1:]))
            
        return total_ones + max_gain;