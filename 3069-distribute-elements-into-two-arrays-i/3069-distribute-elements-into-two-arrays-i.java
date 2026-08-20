class Solution {
    public int[] resultArray(int[] nums) {
        int n = nums.length;
        List<Integer> arr1 = new ArrayList<>();
        List<Integer> arr2 = new ArrayList<>();

        // 1st operation goes to arr1, 2nd operation goes to arr2
        arr1.add(nums[0]);
        arr2.add(nums[1]);

        // Distribute remaining elements based on the last elements
        for (int i = 2; i < n; i++) {
            if (arr1.get(arr1.size() - 1) > arr2.get(arr2.size() - 1)) {
                arr1.add(nums[i]);
            } else {
                arr2.add(nums[i]);
            }
        }

        // Concatenate arr1 and arr2 into the result array
        int[] result = new int[n];
        int index = 0;
        for (int val : arr1) {
            result[index++] = val;
        }
        for (int val : arr2) {
            result[index++] = val;
        }

        return result;
    }
}