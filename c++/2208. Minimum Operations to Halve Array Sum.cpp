//https://leetcode.com/problems/minimum-operations-to-halve-array-sum/description/
class Solution {
public:
    int halveArray(vector<int>& nums) {
        priority_queue<double> heap;        
        double total = 0;
        for(int i=0;i<nums.size();i++){
            heap.push(nums[i]);
            total += nums[i];
        }
        double newTotal = total;
        int op = 0;
        while(total > newTotal/2){
            double top = heap.top();
            heap.pop();
            total -= top/2;
            heap.push(top/2);
            op++;
        }
        return op;
    }
};