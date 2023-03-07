//https://leetcode.com/problems/sort-an-array/description/
class Solution {
public:
    vector<int> sortArray(vector<int>& nums) {
        vector<int> out;
        priority_queue<int,vector<int>,greater<int>>heap(nums.begin(),nums.end());
        while(!heap.empty()){
           out.push_back(heap.top());
           heap.pop();
        }
        return out;
    }
};