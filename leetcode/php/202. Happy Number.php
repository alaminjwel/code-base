<?php
//https://leetcode.com/problems/happy-number/
class Solution {

    /**
     * @param Integer $n
     * @return Boolean
     */
    function isHappy($n) {
        $storage = [];
        while(1){
            $temp = (String) $n;
            $n = 0;
            for($i=0;$i<strlen($temp);$i++){
                $n += $temp[$i]*$temp[$i];
            }
            if($n===1) return true;
            if(in_array($n, $storage)) return false;
            $storage[] = $n;
        }
    }
}