/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        int len = lists.size();
        if(len==0) return NULL;
        priority_queue<int,vector<int>,greater<int>> heap;
        for(int i=0;i<len;i++){
            ListNode* head = lists[i];
            while(head != NULL){
                heap.push(head->val);
                head = head->next;
            }
        }
        ListNode* start = NULL;
        ListNode* end = NULL;
        while(!heap.empty()){
            if(start == NULL){
                 start = new ListNode(heap.top());
                 end = start;
                 heap.pop();
            }
            else{
                end->next = new ListNode(heap.top());
                heap.pop();
                end = end->next;
            }
        }
        return start;
    }
};