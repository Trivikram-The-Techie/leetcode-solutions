class Solution {
    public boolean sumGame(String num) {
        int n = num.length();
        int sumDiff = 0;
        int qDiff = 0;

        for (int i = 0; i < n; i++) {
            int sign = (i < n / 2) ? 1 : -1;
            char c = num.charAt(i);

            if (c == '?') {
                qDiff += sign;
            } else {
                sumDiff += sign * (c - '0');
            }
        }

        // If the total number of '?' is odd, Alice gets the last move and can always win.
        if ((qDiff & 1) != 0) {
            return true;
        }

        // Bob wins if and only if each pair of '?' on the deficit side can compensate for 9 points.
        // That means: sumDiff + (qDiff / 2) * 9 == 0
        return sumDiff * 2 + qDiff * 9 != 0;
    }
}