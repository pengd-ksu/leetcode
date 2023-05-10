#include <vector>
#include <algorithm>
#include <list>

class Solution {
public:
    static bool compare(const std::vector<int>& a, const std::vector<int>& b) {
        return (a[0] == b[0]) ? a[1] < b[1] : a[0] > b[0];
    }
    
    std::vector<std::vector<int>> reconstructQueue(std::vector<std::vector<int>>& people) {
        sort(people.begin(), people.end(), compare);
        std::list<std::vector<int>> output;
        for (const std::vector<int>& p : people) {
            auto it = output.begin();
            advance(it, p[1]);
            output.insert(it, p);
        }
        return std::vector<std::vector<int>>(output.begin(), output.end());
    }
};
