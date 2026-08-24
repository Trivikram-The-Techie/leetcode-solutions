class Solution {
    public int stoneGameVIII(int[] stones) {
        int n = stones.length;
        int[] prefixSum = new int[n];
        prefixSum[0] = stones[0];
        for (int i = 1; i < n; i++) {
            prefixSum[i] = prefixSum[i - 1] + stones[i];
        }

        // dp tracks the maximum net score a player can achieve from index i onwards.
        // Base case: if taking all stones up to the last index (n - 1)
        int dp = prefixSum[n - 1];
        for (int i = n - 2; i >= 1; i--) {
            dp = Math.max(dp, prefixSum[i] - dp);
        }

        return dp;
    }
}