class Solution:

  def uniqueXorTriplets(self, nums: list[int]) -> int:
    n = len(nums)

    # Base cases
    if n == 1:
      return 1
    if n == 2:
      return 2

    # For n >= 3, we can form all integers from 0 to 2^(msb(n) + 1) - 1.
    # The total number of unique XOR values is 2^(bit_length(n)).
    return 1 << n.bit_length()