<?php
//https://leetcode.com/problems/majority-element/
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function majorityElement($nums) {
        $n = count($nums);
        $time = $n/2;
        $freq = [];
        for($i=0;$i<$n;$i++){
           if(!isset($freq[$nums[$i]])) $freq[$nums[$i]] = 0;
           $freq[$nums[$i]] = $freq[$nums[$i]]+1;
           if($freq[$nums[$i]]>$time) return $nums[$i];
        }
        return false;
    }
}


class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function majorityElement($nums) {
        $n = count($nums);
        if($n==1) return $nums[0];
        $time = ($n-1)/2;
        sort($nums);
        return $nums[$time];
    }
}