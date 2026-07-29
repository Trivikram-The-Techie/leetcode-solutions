from collections import Counter

class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        MAX_K = 10**6 + 1
        n = len(s)
        
        # 1. Count character frequencies
        counts = Counter(s)
        
        # Determine frequency for the left half and the middle character (if n is odd)
        half_counts = [0] * 26
        mid_char = ""
        
        for ch, freq in counts.items():
            half_counts[ord(ch) - ord('a')] = freq // 2
            if freq % 2 == 1:
                mid_char = ch

        # Helper to compute nCr capped at MAX_K
        def nCr(n: int, r: int) -> int:
            if r < 0 or r > n:
                return 0
            if r == 0 or r == n:
                return 1
            res = 1
            for i in range(1, min(r, n - r) + 1):
                res = res * (n - i + 1) // i
                if res >= MAX_K:
                    return MAX_K
            return res

        # Helper to calculate the total distinct permutations of remaining counts
        def count_arrangements(freq_list: list[int]) -> int:
            total_len = sum(freq_list)
            res = 1
            for freq in freq_list:
                res *= nCr(total_len, freq)
                if res >= MAX_K:
                    return MAX_K
                total_len -= freq
            return res

        # Check if k exceeds total possible permutations
        total_perms = count_arrangements(half_counts)
        if k > total_perms:
            return ""

        # 2. Construct the left half character by character
        left_half = []
        half_len = sum(half_counts)

        for _ in range(half_len):
            for i in range(26):
                if half_counts[i] == 0:
                    continue
                
                # Try placing character i
                half_counts[i] -= 1
                arrangements = count_arrangements(half_counts)
                
                if arrangements >= k:
                    left_half.append(chr(ord('a') + i))
                    break
                else:
                    k -= arrangements
                    half_counts[i] += 1  # Backtrack and try next character

        # 3. Assemble full palindrome
        left_str = "".join(left_half)
        return left_str + mid_char + left_str[::-1]