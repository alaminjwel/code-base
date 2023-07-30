class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int count = 0;
        for(int i=0;i<nums.size();i++){
            if(nums[i]==val) {
                nums[i] = 51;
                count++;
            }
        }
        sort(nums.begin(),nums.end());
        nums.erase(nums.end()-count,nums.end());
        return nums.size();
    }
};