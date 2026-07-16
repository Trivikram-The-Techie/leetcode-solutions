class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Dictionary to store the number and its index
        num_map = {}
        
        for i, num in enumerate(nums):
            # Calculate the difference needed to hit the target
            complement = target - num
            
            # If the complement is already in our map, we found our pair
            if complement in num_map:
                return [num_map[complement], i]
            
            # Otherwise, add the current number and its index to the map
            num_map[num] = i
            
        return []