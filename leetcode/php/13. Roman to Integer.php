<?php

//https://leetcode.com/problems/roman-to-integer/

class Solution {

    /**
     * @param String $s
     * @return Integer
     */
    function romanToInt($s) {
        $sum = 0;
        for($i=0;$i<strlen($s);$i++){
            $find = ['M','D','C','L','X','V','I',''];
            $replace = [1000,500,100,50,10,5,1,0];
            $next = $s[$i+1] ?? '';
            $cur = str_replace($find,$replace, $s[$i]);
            $next = str_replace($find,$replace,$next);
            if($next>$cur) {
                $sum += $next-$cur;
                $i++;
            }
            else $sum += $cur;
        }
        return $sum;
    }
}