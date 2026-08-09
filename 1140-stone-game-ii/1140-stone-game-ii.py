class Solution:
    def stoneGameII(self, piles: list[int]) -> int:
        n = len(piles)
        
        # Calculate suffix sums to quickly query total remaining stones from index i
        suffix_sum = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix_sum[i] = suffix_sum[i + 1] + piles[i]
            
        memo = {}
        
        def dfs(i: int, m: int) -> int:
            # Base case: if remaining piles can all be taken in one turn
            if i + 2 * m >= n:
                return suffix_sum[i]
            
            if (i, m) in memo:
                return memo[(i, m)]
            
            max_stones = 0
            # Try taking X piles where 1 <= X <= 2 * m
            for x in range(1, 2 * m + 1):
                # Opponent gets the optimal score from state (i + x, max(m, x))
                opponent_stones = dfs(i + x, max(m, x))
                # Current player gets remaining total minus opponent's score
                current_stones = suffix_sum[i] - opponent_stones
                max_stones = max(max_stones, current_stones)
                
            memo[(i, m)] = max_stones
            return max_stones
            
        return dfs(0, 1)