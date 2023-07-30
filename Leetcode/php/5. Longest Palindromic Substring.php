<?php
//https://leetcode.com/problems/longest-palindromic-substring/
class Solution {

    /**
     * @param String $s
     * @return String
     */
    function longestPalindrome($s) {
        $len = strlen($s);
        if($len<=1 || $this->istPalindrome($s)) return $s;
        $longestPalindrome = '';
        for($i=0;$i<$len;$i++){
            $temp = $s[$i];
            if($this->istPalindrome($temp) && strlen($temp)>strlen($longestPalindrome)){
                $longestPalindrome = $temp;
            }
            for($j=$i+1;$j<$len;$j++){               
               $temp .= $s[$j];
               if($this->istPalindrome($temp) && strlen($temp)>strlen($longestPalindrome)){
                    $longestPalindrome = $temp;
               }
            }
        }
        return $longestPalindrome;
    }
    function istPalindrome($s){
        if(empty($s)) return false;
        return $s == strrev($s);
    }
}