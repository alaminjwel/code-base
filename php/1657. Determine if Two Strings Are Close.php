<?php

/*https://leetcode.com/problems/determine-if-two-strings-are-close*/

class Solution {
    /**
     * @param String $word1
     * @param String $word2
     * @return Boolean
     */
    function closeStrings($word1, $word2) {
        $len1 = strlen($word1);
        $len2 = strlen($word2);
        if($len1 != $len2) return false;

        $charCount1 = [];
        $uniqueChar1 = [];
        for($i=0;$i<$len1;$i++){
            $pos = $word1[$i];
            if(!isset($charCount1[$pos])) $charCount1[$pos] = 0;
            $charCount1[$pos]++;
        }

        $charCount2 = [];    
        for($i=0;$i<$len2;$i++){
            $pos = $word2[$i];
            if(!isset($charCount2[$pos])) $charCount2[$pos] = 0;
            $charCount2[$pos]++;
        }

        $haveMutualChats = true;
        foreach ($charCount1 as $key => $value) {
            if(!isset($charCount2[$key])){
                $haveMutualChats = false;
                break;
            }
        }

        sort($charCount1);
        sort($charCount2);
        if($haveMutualChats && $charCount1==$charCount2) return true;
        return false;

    }
}