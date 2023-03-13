class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        """
        # Naive, Time Limit Exceeded
        arr = [0] * length
        for u in updates:
            for i in range(u[0], u[1]+1):
                arr[i] += u[2]
        return arr
        """
        # We only need to update the boundary, and iterate in the final step
        # One step further beyond the boundary should be negative of the update,
        # so that further iteration would remain zero
        arr = [0] * length
        for u in updates:
            arr[u[0]] = arr[u[0]] + u[2]
            if u[1] < length - 1:
                arr[u[1] + 1] = arr[u[1] + 1] - u[2]
        for i in range(1, length):
            arr[i] = arr[i] + arr[i-1]
        return arr