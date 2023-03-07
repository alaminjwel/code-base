class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        priority_queue<int> heap(nums.begin(),nums.end());
        int kthMax = 0;
        while(k--){
            if(k==0) kthMax = heap.top();
            heap.pop();
        }
        return kthMax;        
    }
};