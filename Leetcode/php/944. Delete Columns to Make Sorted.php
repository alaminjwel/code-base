<?php

//https://leetcode.com/problems/delete-columns-to-make-sorted/

class Solution {

    /**
     * @param String[] $strs
     * @return Integer
     */
    function minDeletionSize($strs) {
        $del = 0;
        $count = count($strs);
        for($j=0;$j<strlen($strs[0]);$j++){
            for($i=0;$i<$count-1;$i++){
                if($strs[$i][$j] > $strs[$i+1][$j]){
                    $del++;
                    break;
                }
            }
        }
        return $del;
    }
}