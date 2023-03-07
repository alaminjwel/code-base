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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        int length = 0;

        ListNode *copy = head;
        ListNode *copy2 = head;

        while(head != NULL){
            length++;
            head = head->next;
        }

        if(length==1) return NULL;
        if(length <= n){
            return copy->next;
        }
        
        for(int i=1;i<length-n;i++){
            copy2 = copy2->next;
        }
        copy2->next=copy2->next->next;
        return copy;
    }
};