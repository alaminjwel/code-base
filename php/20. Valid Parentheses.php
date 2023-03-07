<?php
//https://leetcode.com/problems/valid-parentheses/
class Solution {

    /**
     * @param String $s
     * @return Boolean
     */
    function isValid($s) {
        if(in_array($s[0],[')','}',']'])) return false;
        $stack = [];
        for($i=0;$i<strlen($s);$i++){
            if(in_array($s[$i],['(','{','['])) array_push($stack,$s[$i]);
            else if(in_array($s[$i],[')','}',']'])){
                $top = array_pop($stack);
                $top = str_replace(['(','{','['],[')','}',']'],$top);
                if($top != $s[$i]) return false;    
            }
        }
        return empty($stack) ? true : false;
    }
}  