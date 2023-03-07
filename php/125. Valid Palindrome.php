<?php
//https://leetcode.com/problems/valid-palindrome/description/
class Solution {

    /**
     * @param String $s
     * @return Boolean
     */
    function isPalindrome($s) {
        $s = strtolower($s);
        $filtered = '';
        for($i=0;$i<strlen($s);$i++){
            if(($s[$i]>='a' && $s[$i]<='z') || ($s[$i]>='0' && $s[$i]<='9')) 
            $filtered .= $s[$i];
        }
        return $filtered == strrev($filtered);
    }
}