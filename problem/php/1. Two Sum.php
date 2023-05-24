<?php
//https://leetcode.com/problems/two-sum/
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $target
     * @return Integer[]
     */
    function twoSum($nums, $target) {
        $count = count($nums);
        $return = null;
        for($i=0;$i<$count-1;$i++){
            for($j=$i+1;$j<$count;$j++){
                if($nums[$i]+$nums[$j]==$target){
                    $return = [$i,$j];
                    break;
                }
            }
            if(!empty($return)) break;
        }
        return $return;
    }
}