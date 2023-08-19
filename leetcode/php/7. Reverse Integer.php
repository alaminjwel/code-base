<?php
//https://leetcode.com/problems/reverse-integer/
class Solution {

       /**
     * @param Integer $x
     * @return Integer
     */
    function reverse($x) {
        $negative = $x<0 ? true : false;
        $x = strrev($x);
        $x = (int) $x;
        if($negative) $x = 0-$x;
        return $x>2147483647 || $x<-2147483648 ? 0 : $x;
    }
}
