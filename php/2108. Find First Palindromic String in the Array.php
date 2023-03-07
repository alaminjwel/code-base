<?php
//https://leetcode.com/problems/find-first-palindromic-string-in-the-array/description/
class Solution {

    /**
     * @param String[] $words
     * @return String
     */
    function firstPalindrome($words) {
        for($i=0;$i<count($words);$i++){
            if($words[$i] == strrev($words[$i])) return $words[$i];
        }
        return '';
    }
}