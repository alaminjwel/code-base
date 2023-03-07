<?php
//https://leetcode.com/problems/pascals-triangle/
class Solution {

    /**
     * @param Integer $numRows
     * @return Integer[][]
     */
    function generate($numRows) {
        if($numRows==1) return [[1]];
        $rows = [[1],[1,1]];
        if($numRows==2) return $rows;

        for($i=2;$i<$numRows;$i++){
            for($j=0;$j<$i+1;$j++){
                if($j==0 || $j==$i) $rows[$i][$j] = 1;
                else{
                    $rows[$i][$j] =  $rows[$i-1][$j-1] +  $rows[$i-1][$j];
                }
            }
        }
        return $rows;
    }
}