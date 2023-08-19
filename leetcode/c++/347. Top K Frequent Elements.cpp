//https://leetcode.com/problems/top-k-frequent-elements/
class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        priority_queue<pair<int,int>> heap;
        map<int, int> freq;
        vector<int> out;

        for (int i : nums) {
            freq[i] += 1;
        }

        for(auto val: freq){
            heap.push({val.second, val.first});
        }

        while(k--){
            out.push_back(heap.top().second);
            heap.pop();
        }
        return out;

    }
};