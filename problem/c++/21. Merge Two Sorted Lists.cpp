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
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        priority_queue<int,vector<int>,greater<int>> heap;
        
        ListNode* head = list1;
        while(head != NULL){
            heap.push(head->val);
            head = head->next;
        }
        ListNode* head2 = list2;
        while(head2 != NULL){
            heap.push(head2->val);
            head2 = head2->next;
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