<?php
//https://leetcode.com/problems/detect-capital/
class Solution {

    /**
     * @param String $word
     * @return Boolean
     */
    function detectCapitalUse($word) {
        return $word == strtoupper($word) || $word == strtolower($word) || $word == ucfirst(strtolower($word));
    }
}