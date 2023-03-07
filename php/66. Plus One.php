<?php
//https://leetcode.com/problems/plus-one/
class Solution {

    /**
     * @param Integer[] $digits
     * @return Integer[]
     */
    function plusOne($digits) {
        $len = count($digits);
        $result = [];
        $c = $s = 0;
        for ($i=$len-1; $i >= 0 ; $i--) {
            $seed = $i==$len-1 ? 1 : 0;
            $s = $digits[$i] + $c + $seed;
            if($s>9){
                $c = $s/10;
                $s = $s%10;
            }
            else $c = 0;
            $result[] = $s;
        }
        if($c>0) array_push($result, $c);
        $result = array_reverse($result);
        return $result;
    }
}