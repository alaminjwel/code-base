<?php
https://leetcode.com/problems/gas-station/submissions/873461558/
class Solution {

    /**
     * @param Integer[] $gas
     * @param Integer[] $cost
     * @return Integer
     */
    function canCompleteCircuit($gas, $cost) {
        $count = count($gas);
        $start = 0;
        $totalGas = 0;
        $totalCost = 0;
        $totalRemaining = 0;
        for($i=0;$i<$count;$i++){
            $totalGas += $gas[$i];
            $totalCost += $cost[$i];
            $totalRemaining += $gas[$i] - $cost[$i];
            if($totalRemaining<0){
                $start = $i+1;
                $totalRemaining = 0;
            }
        }
        return $totalGas>=$totalCost ? $start : -1;        
       
    }
}