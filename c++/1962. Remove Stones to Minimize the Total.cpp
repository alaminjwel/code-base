//https://leetcode.com/problems/remove-stones-to-minimize-the-total/
class Solution {
public:
    int minStoneSum(vector<int>& piles, int k) {
        priority_queue<int> heap;        
        int total = 0;
        for(int i=0;i<piles.size();i++){
            heap.push(piles[i]);
            total += piles[i];
        }
        for(int i=0;i<k;i++){
            int top = heap.top();
            heap.pop();
            int remove = top/2;
            total -= remove;
            heap.push(top-remove);
        }
        return total;
    }
};