<?php
//https://leetcode.com/problems/maximum-ice-cream-bars/submissions/872630510/
class Solution {

    /**
     * @param Integer[] $costs
     * @param Integer $coins
     * @return Integer
     */
    function maxIceCream($costs, $coins) {
        sort($costs);
        $maxIceCream = 0;
        $spent = 0;
        for($i=0;$i<count($costs);$i++){
            if($spent + $costs[$i] <= $coins) {
                $spent += $costs[$i];
                $maxIceCream++;
            }
            else break;
        }
        return $maxIceCream;
    }
}