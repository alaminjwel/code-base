<?php
//https://leetcode.com/problems/reverse-linked-list/
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
     * @return ListNode
     */

    /* Lets input is [1,2,3,4,5]*/

    /* iteration : 
    the revList head is being updated to latest head of input list 
    and revList next is the previous version of the revList

    revList = [1,null] 
    revList = [2,1,null] (previous version = [1,null])
    revList = [3,2,1,null] (previous version = [2,1,null])
    revList = [4,3,2,1,null] (previous version = [3,2,1,null])
    revList = [5,3,2,1,null] (previous version = [4,3,2,1,null])
    */

    function reverseList($head) {
        $revList = null;
        while($head != null){
            $revList = new ListNode($head->val,$revList);
            $head = $head->next;
        }
        return $revList;
    }
}