from collections import defaultdict
from typing import List


class Solution:

  def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
    occupied = defaultdict(int)

    # Seat 1 and 10 do not affect any 4-person group placement
    for r, c in reservedSeats:
      if 2 <= c <= 9:
        occupied[r] |= 1 << c

    # Rows with no reservations in seats 2-9 can fit 2 families each
    ans = (n - len(occupied)) * 2

    left_mask = (1 << 2) | (1 << 3) | (1 << 4) | (1 << 5)  # seats 2, 3, 4, 5
    right_mask = (1 << 6) | (1 << 7) | (1 << 8) | (1 << 9)  # seats 6, 7, 8, 9
    mid_mask = (1 << 4) | (1 << 5) | (1 << 6) | (1 << 7)  # seats 4, 5, 6, 7

    for mask in occupied.values():
      left_free = not (mask & left_mask)
      right_free = not (mask & right_mask)

      if left_free and right_free:
        ans += 2
      elif left_free or right_free or not (mask & mid_mask):
        ans += 1

    return ans