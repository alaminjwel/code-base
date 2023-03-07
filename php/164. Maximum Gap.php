<?php
//https://leetcode.com/problems/maximum-gap/
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function maximumGap($nums) {
        $count = count($nums);
        if($count<2) return 0;

        sort($nums);

        $maxGap = 0;
        for($i = 0; $i < $count-1; $i++){
            $subs = abs($nums[$i]-$nums[$i+1]);
            if($subs>$maxGap) $maxGap = $subs;
        }
        return $maxGap;

    }
}