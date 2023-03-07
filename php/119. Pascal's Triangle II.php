<?php
//https://leetcode.com/problems/pascals-triangle-ii/
class Solution {

    /**
     * @param Integer $rowIndex
     * @return Integer[]
     */
    function getRow($rowIndex) {
        if($rowIndex==0) return [1];
        if($rowIndex==1) return [1,1];

        $numRows = $rowIndex+1;

        $rows = [[1],[1,1]];
        for($i=2;$i<$numRows;$i++){
            for($j=0;$j<$i+1;$j++){
                if($j==0 || $j==$i) $rows[$i][$j] = 1;
                else{
                    $rows[$i][$j] =  $rows[$i-1][$j-1] +  $rows[$i-1][$j];
                }
            }
        }
        return $rows[$rowIndex];
    }
}