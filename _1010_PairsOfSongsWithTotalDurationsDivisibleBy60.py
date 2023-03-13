class Solution:
    # Brute force. Time Limit Exceeded
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        count = 0
        for i in range(len(time)):
            for j in range(i):
                if (time[i] + time[j]) % 60 == 0:
                    count += 1
        return count

class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        cnt = 0
        record = dict()
        for t in time:
            remainder = t % 60
            if 60 - remainder in record.keys():
                cnt += record[60 - remainder]
            elif remainder == 0 and 0 in record.keys():
                cnt += record[0]
            record[remainder] = record.get(remainder, 0) + 1
        return cnt