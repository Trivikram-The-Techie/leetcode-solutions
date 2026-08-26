import java.util.ArrayList;
import java.util.List;

class Solution {
    public String shortestBeautifulSubstring(String s, int k) {
        List<Integer> ones = new ArrayList<>();
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == '1') {
                ones.add(i);
            }
        }

        // If there are fewer than k '1's in total
        if (ones.size() < k) {
            return "";
        }

        String ans = "";

        // Any shortest beautiful substring must start and end with '1'
        for (int i = 0; i + k - 1 < ones.size(); i++) {
            int left = ones.get(i);
            int right = ones.get(i + k - 1);
            String sub = s.substring(left, right + 1);

            if (ans.isEmpty() || sub.length() < ans.length() || 
               (sub.length() == ans.length() && sub.compareTo(ans) < 0)) {
                ans = sub;
            }
        }

        return ans;
    }
}