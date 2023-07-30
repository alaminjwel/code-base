<?php
// https://leetcode.com/problems/middle-of-the-linked-list/
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
    function middleNode($head) {
        $items = [$head];
        while($head){
            $items[] = $head;
            $head = $head->next;
        };
        return $items[ceil(count($items)/2)];
    }
}
