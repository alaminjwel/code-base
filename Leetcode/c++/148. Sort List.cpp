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
    ListNode* sortList(ListNode* head) {
        priority_queue<int,vector<int>,greater<int>> heap;
        while(head){
            heap.push(head->val);
            head = head->next;
        }
        ListNode* start = NULL;
        ListNode* end = NULL;
        while(!heap.empty()){
            if(start == NULL){
                start = new ListNode(heap.top());
                end = start;
            }
            else{
                end->next = new ListNode(heap.top());
                end = end->next;
            }
            heap.pop();
        }
        return start;
    }
};