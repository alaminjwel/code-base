<?php
//https://leetcode.com/problems/string-to-integer-atoi/
class Solution {

    /**
    * @param String $s
    * @return Integer
    */
    function myAtoi($s) {
        $s = trim($s);
        $number = '';
        $isNegative = false;
        for($i=0;$i<strlen($s);$i++){
            if($i==0) {
                if($s[$i] == '-') $isNegative = true;
                else if($s[$i] == '+') $isNegative = false;
                else if($this->isDigit($s[$i])) $number .= $s[$i];            
                else break;
            }
            else{
                if($this->isDigit($s[$i])) $number .= $s[$i];                
                else break;
            }
        }
        $number = ltrim($number,'0');
        if(empty($number)) return 0;
        if($isNegative) $number = 0-$number;

        if($number>2147483647) $number = 2147483647;
        else if($number<-2147483648) $number = -2147483648;
        return $number;
    }

    function isDigit($s){
        return $s == '0' || $s == '1' || $s == '2' || $s == '3' || $s == '4' || $s == '5' || $s == '6' || $s == '7' || $s == '8' || $s == '9';
    }
}