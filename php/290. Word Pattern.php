<?php
//https://leetcode.com/problems/word-pattern/
class Solution {

    /**
     * @param String $pattern
     * @param String $s
     * @return Boolean
     */
    function wordPattern($pattern, $s) {
        $len = strlen($pattern);

        $map = [];
        $map2 = [];
        $exp = explode(' ', $s);
        for($i=0;$i<$len;$i++){
            $map[$pattern[$i]][] = $i;
        }

        for($i=0;$i<count($exp);$i++){
            $map2[$exp[$i]][] = $i;
        }
        
        $map_count = count($map);
        if($map_count != count($map2)) return false;

        foreach ($map as $key => $value) {
            $match = $exp[$value[0]];
            if($value != $map2[$match]) return false;
        }
        return true;
    }
}