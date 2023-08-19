//https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/description/
class Solution {
public:
    int kthSmallest(vector<vector<int>>& matrix, int k) {
        priority_queue <int> heap;

        for (auto row : matrix){
            for (auto col : row){
                heap.push(col);
                if(heap.size()>k) heap.pop();
            }
        }
            
        return heap.top();
    }
};