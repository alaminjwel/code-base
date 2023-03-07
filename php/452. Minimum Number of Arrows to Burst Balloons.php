<?php
//https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/
class Solution {

    /**
     * @param Integer[][] $points
     * @return Integer
     */
    function findMinArrowShots($points) {
        $count = count($points);
        if($count==1) return 1;
        usort($points, function($a, $b) {
            return $a[0] <=> $b[0];
        });

        $shot = $points[0][1];
        $shotCount=1;
        for($i=1;$i<$count;$i++){
            if($points[$i][0] > $shot){
                $shot = $points[$i][1];
                $shotCount++;
            }
            else{
                $shot =  min($points[$i][1],$shot);
            }
        }
        return $shotCount;
    }
}