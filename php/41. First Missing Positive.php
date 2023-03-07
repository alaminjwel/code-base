<?php
/*https://leetcode.com/problems/first-missing-positive*/

class Solution {
    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function firstMissingPositive($nums) {
        sort($nums);
        $max = $nums[0];
        $mappedNums = [];
        for($i=0;$i<count($nums);$i++){
            if($nums[$i]>$max && $i>0) $max = $nums[$i];
            if($nums[$i]>0) $mappedNums[$nums[$i]] = $nums[$i];
        }
        if($max<1) return 1;
        $find = 1;
        for($i=1;$i<=$max+1;$i++){
            if(!isset($mappedNums[$i])){
                $find = $i;
                break;
            }
        }        
        return $find;
    }

}