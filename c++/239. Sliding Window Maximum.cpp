/*The elements in the deque q that are smaller than the current element nums[i] are popped from the back of the deque.
The current index i is pushed to the back of the deque.
If the current index i is greater than or equal to k-1, the front of the deque (which contains the maximum value in the current window) is added to the output array out.
If the front of the deque is outside the current window (i.e. q.front() <= i-k + 1), it is popped from the front of the deque.
Explain : https://www.youtube.com/watch?v=DfljaUwZsOk&t=815s
*/

class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        vector<int> out; // Vector to store the result
        deque<int> q; // Deque to store indices of elements in the sliding window
        
        // Loop through all elements in the array
        for(int i=0;i<nums.size();i++){
            
            // Pop elements from the back of the deque that are smaller than the current element
            while(!q.empty() && nums[i] >= nums[q.back()]) q.pop_back();
            
            // Push the current index to the back of the deque
            q.push_back(i);
            
            // If we have processed k elements, add the front of the deque (maximum element) to the result
            if(i >= k-1) out.push_back(nums[q.front()]);
            
            // Pop the front of the deque if it is outside the current window
            if(q.front()<= i-k + 1) q.pop_front();
        }
        return out; // Return the result
    }
};
