<?php

/*https://leetcode.com/problems/determine-if-string-halves-are-alike/*/

class Solution {
    /**
     * @param String $s
     * @return Boolean
     */
    function halvesAreAlike($s) {
        $len = strlen($s);
        if($len %2 != 0 || $len<2 || $len>1000) return false;
        $spl = str_split($s,($len/2));
        $fst = $spl[0];
        $snd = $spl[1];
        return $this->countVowels($fst) == $this->countVowels($snd);        
    }

    function countVowels($s){
        $vowels = ['a','e','i','o','u'];
        $count=0;
        for($i=0;$i<strlen($s);$i++){
            if(in_array(strtolower($s[$i]),$vowels)) $count++;
        }
        return $count;
    }
}