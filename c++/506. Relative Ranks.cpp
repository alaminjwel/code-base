//https://leetcode.com/problems/relative-ranks/description/
class Solution {
public:
    vector<string> findRelativeRanks(vector<int>& score) {
        priority_queue<pair<int,int>> heap;
        map<int,int> scoreMap;
        vector<string> out(score.size(),"");

        for(int i=0;i<score.size();i++){
            heap.push(make_pair(score[i],i));
        }

        int rank = 1;
        while(!heap.empty()){
           int index = heap.top().second;
           if(rank==1) out[index] = "Gold Medal";           
           else if(rank==2) out[index] = "Silver Medal";           
           else if(rank==3) out[index] = "Bronze Medal";
           else out[index] = to_string(rank);
           rank++;
           heap.pop();
        }
        return out;
        
    }
};