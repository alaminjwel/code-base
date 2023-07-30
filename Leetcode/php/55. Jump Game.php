<?php
//https://leetcode.com/problems/jump-game/
class Solution {
    function canJump($nums) {
        $len = count($nums);
        $goal = $len-1;
        for($i=$len-2;$i>=0;$i--){
            $jump = $goal-$i;
            if($nums[$i]>=$jump) $goal = $i;
        }
        return $goal == 0;
    }

}