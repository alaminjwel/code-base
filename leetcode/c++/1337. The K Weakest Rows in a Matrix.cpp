class Solution {
public:
    vector<int> kWeakestRows(vector<vector<int>>& mat, int k) {
        priority_queue<pair<int,int>,vector<pair<int,int>>,greater<pair<int,int>>> heap;
        vector<int> out;
        for(int i=0;i<mat.size();i++){
            int sum = accumulate(mat[i].begin(),mat[i].end(),0);
            heap.push(make_pair(sum,i));
        }
        while(k--){
            out.push_back(heap.top().second);
            heap.pop();
        }
        return out;
    }
};