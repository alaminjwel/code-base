<?php
//https://leetcode.com/problems/length-of-last-word/
class Solution {

    /**
     * @param String $s
     * @return Integer
     */
    function lengthOfLastWord($s) {
        $exp = explode(' ',trim($s));
        $last = array_pop($exp);
        return strlen($last);
    }
}