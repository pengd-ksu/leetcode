#include <iostream>
#include <vector>
#include <algorithm>

class Solution {
public:
    std::vector<std::vector<int>> minimumAbsDifference(std::vector<int>& arr) {
        std::sort(arr.begin(), arr.end());
        std::vector<std::vector<int>> res;
        int minPair = INT_MAX;
        for (int i = 0; i < arr.size() - 1; i++) {
            minPair = std::min(minPair, arr[i+1] - arr[i]);
        }
        for (int i = 0; i < arr.size() - 1; i++) {
            if (arr[i+1] - arr[i] == minPair) {
                res.push_back({arr[i], arr[i+1]});
            }
        }
        return res;
    }
};