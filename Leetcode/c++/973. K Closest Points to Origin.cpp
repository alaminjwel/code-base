class Solution {
public:
    vector<vector<int>> kClosest(vector<vector<int>>& points, int k) {
        priority_queue< pair<long double,vector<int>>, vector<pair<long double,vector<int>>>, greater<pair<long double,vector<int>>> > heap;
        vector<vector<int>> kclosest(k, vector<int> (2, 0));

        for(int i=0;i<points.size();i++){
            long double dis = sqrtl(abs(pow(points[i][0],2)) + abs(pow(points[i][1],2)));
            heap.push(make_pair(dis,points[i]));
        }
        int i = 0;
        while(k--){
            kclosest[i] = heap.top().second;
            heap.pop();
            i++;
        }
        return kclosest;
    }
};