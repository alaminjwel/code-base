<?php
// https://leetcode.com/problems/minimum-average-difference/
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function minimumAverageDifference($nums) {
        $countNums = count($nums);
        if($countNums<=1) return 0;

        $allSum = 0;
        for($i=0;$i<$countNums;$i++){
            $allSum += $nums[$i];
        }

        $allSum2 = 0;
        $sumMap = [];
        for($i=0;$i<$countNums;$i++){
            $temp = $allSum - $nums[$i];
             $allSum2 += $nums[$i];
             $sumMap[$i] = $allSum- $allSum2;
        }

        $sum1 = 0; 
        $avgMap = 0;
        $pos = 0;
        $iRev=$countNums;
        for($i=0;$i<$countNums;$i++){
            $iRev--;
            $sum1 = $i==0 ? $nums[$i] : $sum1+$nums[$i];
            $operand1 = $sum1==0 || ($i+1)== 0 ? 0 : floor($sum1/($i+1));
            $operand2 =  $sumMap[$i]>0 && $iRev>0 ? floor($sumMap[$i]/$iRev) : 0;
            $calc = abs($operand1-$operand2);
            if($i==0) {
                $avgMap = $calc;
                continue;
            }
            if($calc>=$avgMap) continue;
            $avgMap = $calc;
            $pos = $i;
            
        }
        return $pos;
    }
}