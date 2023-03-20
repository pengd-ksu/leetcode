class Solution {
    public int openLock(String[] deadends, String target) {
        String curr = "0000";
        int step = 0;
        int l = curr.length();
        Set<String> visited = new HashSet<>();
        Set<String> dead = new HashSet<>();
        Queue <String> q = new LinkedList<>();
        q.add(curr);
        q.add(null);
        visited.add(curr);
        for (String deadone : deadends) {
            dead.add(deadone);
        }
        while (!q.isEmpty()) {
            curr = q.poll();
            // Met null, therefore current layer has all made next move and add to queue
            if (curr == null) {
                step += 1;
                // Check if this is the tail in the queue.
                if (q.peek() != null) {
                    q.add(null);
                }
                continue;
            } else if (curr.equals(target)) {
                return step;
            } else if (!dead.contains(curr)) {
                // For the corner case that we don't start from a deadend.
                for (int i = 0; i < l; i++) {
                    for (int move = -1; move <= 1; move += 2) {
                        int next = (curr.charAt(i) - '0' + move + 10) % 10;
                        String nextString = curr.substring(0,i) + String.valueOf(next) + curr.substring(i+1,l);
                        if (!visited.contains(nextString)) {
                            q.add(nextString);
                            visited.add(nextString);
                        }
                    }
                }
            }
            // Previously, I mistakenly added null here. It's wrong because every current
            // move needs to make next step, which all correspond to one further step.
            // q.add(null);
        }
        return -1;
    }
}