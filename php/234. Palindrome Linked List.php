<?php
//https://leetcode.com/problems/palindrome-linked-list/
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
     * @param ListNode $head
     * @return Boolean
     */
    function isPalindrome($head) {
        $nums = '';
        while($head != null){
            $nums .= $head->val;
            $head = $head->next;
        }
        return $nums == strrev($nums);
    }
}