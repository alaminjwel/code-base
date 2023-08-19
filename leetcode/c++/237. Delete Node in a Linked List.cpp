/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 Basically we are just copying node's next value to itself
 Input: 4->5->1->9, given node = 5
 Replace 5 by 1 and replace 1 by 9
 The head was 4 and remains and we do not have the head, we just modify the part staring from node.
 The output: 4->1->9
 */
class Solution {
public:
    void deleteNode(ListNode* node) {
        node->val = node->next->val;
        node->next = node->next->next;
    }
};