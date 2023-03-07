<?php
//https://leetcode.com/problems/remove-duplicates-from-sorted-array/
class Solution {
    /**
     * @param Integer[] $digits
     * @return Integer[]
     */
    function removeDuplicates(&$nums) {
        $count = count($nums);
        for($i=0;$i<$count;$i++){
            if($i+1<$count && $nums[$i] == $nums[$i+1]) unset($nums[$i]);
        }
        return count($nums);
    }
}