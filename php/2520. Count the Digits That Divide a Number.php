<?php
class Solution {

    /**
     * @param Integer $num
     * @return Integer
     */
    function countDigits($num) {
        $str = strval($num); 
        $len = strlen($str);
        if($len==1) return true;

        $count = 0;
        $map = [];
        for($i=0;$i<$len;$i++){
            if($num%$str[$i] == 0 && !isset($map[$i])) {
                $map[$i] = true;
                $count++;
            }
        }
        return $count;
    }
}