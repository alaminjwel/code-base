<?php
//https://leetcode.com/problems/best-time-to-buy-and-sell-stock/submissions/871482091/
class Solution {

    /**
     * @param Integer[] $prices
     * @return Integer
     */
    function maxProfit($prices) {
        $maxProfit = 0;
        $minPrice = $prices[0];
        $count = count($prices);
        for($i=1;$i<$count;$i++){
            $curPrice = $prices[$i];
            if($curPrice<$minPrice) $minPrice = $curPrice;
            else{
                $tmp = $prices[$i]-$minPrice;
                if($tmp>$maxProfit) $maxProfit = $tmp;
            }
        
        }
        return $maxProfit; 
    }
}