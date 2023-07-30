<?php
//https://leetcode.com/problems/add-two-numbers/
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
     * @param ListNode $l1
     * @param ListNode $l2
     * @return ListNode
     */
    function addTwoNumbers($l1, $l2) {
        $num1 = [];
        while($l1 != null){  
            $num1[] = $l1->val;          
            $l1 = $l1->next;
        }

        $num2 = [];
        while($l2 != null){  
            $num2[] = $l2->val;          
            $l2 = $l2->next;
        }
        
        $len1 = count($num1);
        $len2 = count($num2);
        $len = $len1>$len2 ? $len1 : $len2;
        $car = 0;
        $sum = [];
        for($i=0;$i<$len;$i++){
            $dig1 = $num1[$i] ?? 0;
            $dig2 = $num2[$i] ?? 0;
            $tem = $dig1+$dig2+$car;
            if($tem>9) {
                $s = $tem%10;
                $car = floor($tem/10);
            }
            else{
                $s = $tem;
                $car = 0;
            }
            $sum[] = $s;
        }

        if($car>0) {
            $sum[] = $car;
            $len++;
        }

        $head = new ListNode($sum[0],null);
        $cur = $head;
        for($i=1;$i<$len;$i++){
            $cur->next = new ListNode($sum[$i],null);
            $cur = $cur->next;
        }
        return $head;
    }
}