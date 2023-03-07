<?php
//https://leetcode.com/problems/minimum-rounds-to-complete-all-tasks/
class Solution {

    /**
     * @param Integer[] $tasks
     * @return Integer
     */
    function minimumRounds($tasks) {
        print_r($tasks);
        $count = count($tasks);
        $map = [];
        for($i=0;$i<$count;$i++) { 
           $map[$tasks[$i]][$i] = $i;
        }

        $round = 0;
        foreach ($map as $key => $value) {
            $count_item = count($value);
            if($count_item<2) return -1;

            if($count_item>3){
                $round = $round + ceil($count_item/3);
            }
            else $round++;
        }
        return (int) $round;
    }
}