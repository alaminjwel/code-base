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
    ListNode* swapPairs(ListNode* head) {
        if(head == NULL) return NULL;
        vector<int> swap;
        while(head){
            swap.push_back(head->val);
            head = head->next;
        }
        for(int i=0;i<swap.size()-1;i+=2){
            int t1 = swap[i];
            int t2 = swap[i+1];
            swap[i] = t2;
            swap[i+1] = t1;
        }
        ListNode* start = NULL;
        ListNode* end = NULL;
        for(auto x : swap){
            if(start == NULL){
                start = new ListNode(x);
                end = start;
            }
            else{
                end->next = new ListNode(x);
                end = end->next;
            }
        }
        return start;
    }
};