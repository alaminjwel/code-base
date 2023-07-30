class Solution {
public:
   vector<int> sortArrayByParity(vector<int>& nums) {
   int len = nums.size();
   if(len==1) return nums;
   int j= 0;
   for(int i=0;i<len;i++){
      if(nums[i]%2 ==0) {
        swap(nums[i],nums[j]);
        j++;
      }
   }
   return nums;
 }
};



// class Solution {
// public:
//    vector<int> sortArrayByParity(vector<int>& nums) {
//    vector<int> out;
//    int len = nums.size();
//    if(len==1) return nums;
//    for(int i=0;i<len;i++){
//       if(nums[i]%2 !=0) out.push_back(nums[i]);
//       else out.insert(out.begin(), nums[i]);
//    }
//    return out;
//  }
// };