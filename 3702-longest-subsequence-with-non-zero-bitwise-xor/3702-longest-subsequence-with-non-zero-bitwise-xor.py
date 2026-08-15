from functools import reduce
from operator import xor
from typing import List

class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        total_xor = reduce(xor, nums)
        
        # If total XOR is already non-zero, take the whole array
        if total_xor != 0:
            return len(nums)
        
        # If total XOR is 0, check if there is any non-zero element
        if any(x != 0 for x in nums):
            return len(nums) - 1
            
        # All elements are 0
        return 0