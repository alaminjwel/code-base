<?php
//https://leetcode.com/problems/palindrome-number/
class Solution {

/**
 * @param Integer $x
 * @return Boolean
 */
function isPalindrome($x) {
    if($x<0) return false;
    $rev = 0;
    $n = $x;
    while(floor($x)){
        $mod = $x%10;
        $rev = $rev*10+$mod;
        $x = $x/10;
    }
    return $rev==$n;
}