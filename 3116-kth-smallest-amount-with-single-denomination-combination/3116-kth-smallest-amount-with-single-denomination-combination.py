import math
from itertools import combinations
from typing import List

class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        # Optimization: Remove coins that are multiples of smaller coins
        coins.sort()
        filtered_coins = []
        for coin in coins:
            if all(coin % c != 0 for c in filtered_coins):
                filtered_coins.append(coin)
        coins = filtered_coins

        # Helper to compute LCM of an iterable
        def get_lcm(subset):
            res = subset[0]
            for num in subset[1:]:
                res = (res * num) // math.gcd(res, num)
            return res

        # Precompute LCMs grouped by subset size parity
        subsets_lcm = []
        n = len(coins)
        for size in range(1, n + 1):
            sign = 1 if size % 2 == 1 else -1
            for comb in combinations(coins, size):
                subsets_lcm.append((get_lcm(comb), sign))

        # Count distinct values <= m using PIE
        def count(m: int) -> int:
            total = 0
            for lcm_val, sign in subsets_lcm:
                total += sign * (m // lcm_val)
            return total

        # Binary search for the smallest amount with count(m) >= k
        left = min(coins)
        right = min(coins) * k

        while left < right:
            mid = (left + right) // 2
            if count(mid) >= k:
                right = mid
            else:
                left = mid + 1

        return left