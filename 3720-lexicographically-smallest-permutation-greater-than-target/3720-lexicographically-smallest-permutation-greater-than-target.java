class Solution {
    public String lexGreaterPermutation(String s, String target) {
        int n = s.length();
        int[] count = new int[26];
        for (int i = 0; i < n; i++) {
            count[s.charAt(i) - 'a']++;
        }
        int matchLen = 0;
        int[] tempCount = count.clone();
        while (matchLen < n && tempCount[target.charAt(matchLen) - 'a'] > 0) {
            tempCount[target.charAt(matchLen) - 'a']--;
            matchLen++;
        }
        for (int i = Math.min(matchLen, n - 1); i >= 0; i--) {
            int[] currentCount = count.clone();
            for (int j = 0; j < i; j++) {
                currentCount[target.charAt(j) - 'a']--;
            }
            int targetChar = target.charAt(i) - 'a';
            for (int c = targetChar + 1; c < 26; c++) {
                if (currentCount[c] > 0) {
                    currentCount[c]--;
                    StringBuilder sb = new StringBuilder();
                    sb.append(target, 0, i);
                    sb.append((char) ('a' + c));
                    for (int ch = 0; ch < 26; ch++) {
                        while (currentCount[ch] > 0) {
                            sb.append((char) ('a' + ch));
                            currentCount[ch]--;
                        }
                    }
                    return sb.toString();
                }
            }
        }
        return "";
    }
}