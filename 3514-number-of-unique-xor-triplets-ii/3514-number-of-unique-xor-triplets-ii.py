class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        U = set(nums)
        
        # Round 2: Pairwise XORs
        S2 = {a ^ b for a in U for b in U}
        
        # Round 3: Triplet XORs
        S3 = {x ^ c for x in S2 for c in U}
        
        return len(S3);