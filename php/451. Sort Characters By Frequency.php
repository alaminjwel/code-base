<?php
/*https://leetcode.com/problems/sort-characters-by-frequency*/
class Solution {
    /**
     * @param String $word1
     * @param String $word2
     * @return Boolean
     */
    function frequencySort($s) {
        $l = strlen($s);

        $frq = [];
        for($i=0;$i<$l;$i++){
            $pos = $s[$i];
            if(!isset($frq[$pos])) $frq[$pos] = 0;
            $frq[$pos]++;
        }
        arsort($frq);
        $str = '';
        foreach ($frq as $key => $value) {
            for($i=1;$i<=$value;$i++){
                $str .= $key;
            }
        }

        return $str;

    }
}