<?php
//https://leetcode.com/problems/third-maximum-number/
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function thirdMax($nums) {
        $count = count($nums);
        if($count==1) return $nums[0];
        $nums = array_unique($nums);
        sort($nums);
        $count = count($nums);
        if($count==1) return $nums[0];
        $first = array_pop($nums);
        if($count==2) return $first;
        array_pop($nums);
        return array_pop($nums);
    }
}