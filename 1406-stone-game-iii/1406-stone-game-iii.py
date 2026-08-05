from functools import lru_cache

class Solution:
    def stoneGameIII(self, stoneValue: list[int]) -> str:
        n = len(stoneValue)
        
        @lru_cache(None)
        def maxDiff(i: int) -> int:
            if i == n:
                return 0
            
            # Choice 1: Take 1 stone
            res = stoneValue[i] - maxDiff(i + 1)
            
            # Choice 2: Take 2 stones
            if i + 1 < n:
                res = max(res, stoneValue[i] + stoneValue[i + 1] - maxDiff(i + 2))
                
            # Choice 3: Take 3 stones
            if i + 2 < n:
                res = max(res, stoneValue[i] + stoneValue[i + 1] + stoneValue[i + 2] - maxDiff(i + 3))
                
            return res

        diff = maxDiff(0);
        
        if diff > 0:
            return "Alice"
        elif diff < 0:
            return "Bob"
        else:
            return "Tie"