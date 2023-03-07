class Solution {
public:
    int dominantIndex(vector<int>& nums) {
        priority_queue<pair<int,int>> heap;
        for(int i=0;i<nums.size();i++){
            heap.push(make_pair(nums[i],i));
        }
        int max = heap.top().first;
        int maxIndex = heap.top().second;
        heap.pop();
        return max >= heap.top().first * 2 ? maxIndex : -1;
    }
};