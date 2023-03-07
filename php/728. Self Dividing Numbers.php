<?php

class Solution {

    /**
     * @param Integer $left
     * @param Integer $right
     * @return Integer[]
     */
    function selfDividingNumbers($left, $right) {
        $out=[];
        for($i=$left;$i<=$right;$i++){
            if($this->checkNumber($i)) $out[] = $i;
        }
        return $out;
    }

    function checkNumber($num){
        $str = strval($num); 
        for($i=0;$i<strlen($str);$i++){
            if($str[$i]=='0') return false;
            if($num%$str[$i] != 0) return false;
        }
        return true;
    }
}