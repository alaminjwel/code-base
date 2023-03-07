<?php
//https://leetcode.com/problems/longest-common-prefix/
class Solution {

    /**
     * @param String[] $strs
     * @return String
     */
    function longestCommonPrefix($strs) {
        $pr = '';
        $count = count($strs);
        for($i=0;$i<strlen($strs[0]);$i++){
            $matched_count = 0;            
            for($j=1;$j<$count;$j++){
                if(isset($strs[$j][$i]) && $strs[0][$i] == $strs[$j][$i]) 
                $matched_count++;                
            }
            if($matched_count==$count-1) $pr .= $strs[0][$i];
            else break;
        }
        return $pr;
    }
}