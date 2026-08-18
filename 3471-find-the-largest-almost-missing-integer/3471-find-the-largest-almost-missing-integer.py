from collections import defaultdict
from typing import List


class Solution:

  def largestInteger(self, nums: List[int], k: int) -> int:
    n = len(nums)
    subarray_count = defaultdict(int)

    # Count how many subarrays of size k contain each unique integer
    for i in range(n - k + 1):
      seen = set(nums[i : i + k])
      for val in seen:
        subarray_count[val] += 1

    # Find the largest integer that appeared in exactly 1 subarray
    ans = -1
    for val, count in subarray_count.items():
      if count == 1 and val > ans:
        ans = val

    return ans