/* This solution is too slow and can't pass all the tests
 * due to time limit
 * 
 * class Solution {
    public long maxP = 0;

    public void helper(int[][] q, int pos, long curr) {
        if (pos >= q.length) {
            maxP = Math.max(maxP, curr);
            return;
        }
        helper(q, pos + q[pos][1] + 1, curr + q[pos][0]);
        helper(q, pos + 1, curr);
    }

    public long mostPoints(int[][] questions) {
        helper(questions, 0, 0);
        return maxP;
    }
}
 * 
 */
class Solution {
    public long mostPoints(int[][] questions) {
        // For a later one, it might take only one of potentials
        // from previous ones. Therefore, we take it backwards
        int n = questions.length;
        long[] dp = new long[n];
        dp[n - 1] = questions[n - 1][0];
        for (int i = n - 2; i >= 0; i--) {
            dp[i] = questions[i][0];
            int skip = questions[i][1];
            if (i + skip + 1 < n) {
                dp[i] += dp[i + skip + 1];
            }
            // On the other hand, if we skip problem i, the maximum 
            // points we get is the same as the case for i + 1
            dp[i] = Math.max(dp[i], dp[i+1]);
        }
        return dp[0];
    }
}

