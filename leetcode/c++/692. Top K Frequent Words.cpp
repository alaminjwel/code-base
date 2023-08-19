class Solution {
public:
    struct Comp {
        bool operator()(const pair<int, string>& lhs, const pair<int, string>& rhs) const {
            if (lhs.first != rhs.first) return lhs.first < rhs.first;
            return lhs.second > rhs.second;
        }
    };
    vector<string> topKFrequent(vector<string>& words, int k) {
        priority_queue<pair<int,string>,vector<pair<int,string>>,Comp> heap;
        unordered_map<string,int> freq;
        vector<string> out;

        for (auto i : words) {
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