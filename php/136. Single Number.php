<?php
//https://leetcode.com/problems/single-number/
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function singleNumber($nums) {
        $freq = [];
        for($i=0;$i<count($nums);$i++){
            if(!isset($freq[$nums[$i]])) $freq[$nums[$i]] = 1;
            else $freq[$nums[$i]] = $freq[$nums[$i]]+1;
        }
        print_r($freq);
        for($i=0;$i<count($nums);$i++){
           if($freq[$nums[$i]]===1) return $nums[$i];
        }
        return 1;
    }
}