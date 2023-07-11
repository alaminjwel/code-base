class Solution {
public:
    vector<int> kthSmallestPrimeFraction(vector<int>& arr, int k) {
        priority_queue<pair<float,pair<int,int>>> heap;
        int len = arr.size();
        for(int i=0;i<len-1;i++){
            for(int j=i+1;j<len;j++){
                heap.push(make_pair((float)arr[i]/arr[j],make_pair(arr[i],arr[j])));
                if(heap.size()>k) heap.pop();
            }
        }
        return {heap.top().second.first,heap.top().second.second};       
    }
};