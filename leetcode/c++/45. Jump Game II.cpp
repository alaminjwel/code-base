class Solution {
public:
    int jump(vector<int>& nums) {
        // get the length of the input array
        int len = nums.size();
        // if the length is 1, return 0 since there's no need to jump
        if (len == 1) return 0;
        
        // set the goal position to be the end of the array
        int goal = len-1;
        // initialize the current position to be the start of the array
        int pos = 0;
        // initialize the jump count to be 0
        int jumpCount = 0;
        
        // repeat the following steps until the current position reaches the end of the array
        while (pos < goal) {
            // calculate the maximum reachable position from the current position
            int maxReach = pos + nums[pos];
            // if the maximum reachable position is already the end of the array, increment the jump count and break the loop
            if (maxReach >= goal) {
                jumpCount++;
                break;
            }
            
            // initialize the next position to be the current position
            int nextPos = pos;
            // loop through all the positions reachable from the current position
            for (int i = pos + 1; i <= maxReach; i++) {
                // if a new position is
                // found that can reach further than the current next position, update the next position
                if (i + nums[i] > nextPos + nums[nextPos]) {
                    nextPos = i;
                }
            }
            // set the current position to be the new position
            pos = nextPos;
            // increment the jump count
            jumpCount++;
        }
        return jumpCount;
    }
};
