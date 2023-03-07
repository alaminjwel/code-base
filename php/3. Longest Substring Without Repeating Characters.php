<?php
//https://leetcode.com/problems/longest-substring-without-repeating-characters/
class Solution {

    /**
     * @param String $s
     * @return Integer
     */
    function lengthOfLongestSubstring($s) {
        $len = strlen($s);
        $longest = '';
        $longestLength = 0;
        for($i=0;$i<$len;$i++){
            $temp = $s[$i];
            for($j=$i+1;$j<$len;$j++){
               if(str_contains($temp, $s[$j])) break;
               $temp .= $s[$j];
            }
            $curLen = strlen($temp);
            if($curLen>strlen($longest)) {
                $longest = $temp;
                $longestLength = $curLen;
            }
        }
        return $longestLength;
    }
}