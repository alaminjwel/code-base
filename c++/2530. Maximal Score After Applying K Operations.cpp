class Solution {
public:    
    long long maxKelements(vector<int>& nums, int k) {
        priority_queue<int> heap(nums.begin(),nums.end());
        long long total = 0;
        for(int i=0;i<k;i++){
            int top = heap.top();
            total += top;
            top = top%3==0 ? top/3 : top/3+1;
            heap.pop();
            heap.push(top);            
        }
        return total;
    }
};