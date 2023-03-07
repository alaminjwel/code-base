<?php
https://leetcode.com/problems/merge-two-sorted-lists/submissions/866550657/

/**
 * Definition for a singly-linked list.
 * class ListNode {
 *     public $val = 0;
 *     public $next = null;
 *     function __construct($val = 0, $next = null) {
 *         $this->val = $val;
 *         $this->next = $next;
 *     }
 * }
 */
class Solution {

    /**
     * @param ListNode $list1
     * @param ListNode $list2
     * @return ListNode
     */
    function mergeTwoLists($list1, $list2) {
       if($list1 == null) return $list2;
        else if($list2 == null) return $list1;
        
        $head = new ListNode(-1);
        $cur = $head;
        while($list1 != null && $list2 != null) {
            $cur->next = $list1->val <= $list2->val ? $list1 : $list2;
            $cur = $cur->next;

            if($cur->val == $list1->val) $list1 = $list1->next;
            else $list2 = $list2->next;
            
        }
        $cur->next = $list1 != null ? $list1 : $list2;
        return $head->next; 
    }
}