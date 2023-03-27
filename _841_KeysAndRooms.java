class Solution {
    private void dfs(int key, Set<Integer> visited, List<List<Integer>> rooms) {
        visited.add(key);
        for (int newK : rooms.get(key)) {
            if (!visited.contains(newK)) {
                visited.add(newK);
                dfs(newK, visited, rooms);
            }
        }
    }

    public boolean canVisitAllRooms(List<List<Integer>> rooms) {
        Set<Integer> visited = new HashSet<>();
        visited.add(0);
        for (int k : rooms.get(0)) {
            dfs(k, visited, rooms);
        }
        return visited.size() == rooms.size();
    }
}