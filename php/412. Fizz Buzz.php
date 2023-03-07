<?php
//https://leetcode.com/problems/fizz-buzz/
class Solution {

    /**
     * @param Integer $n
     * @return String[]
     */
    function fizzBuzz($n) {
        $result = [];
        for($i=1;$i<=$n;$i++){
            if($i%3==0 && $i%5==0) $result[] = "FizzBuzz";
            elseif($i%3==0) $result[] = "Fizz";
            elseif($i%5==0) $result[] = "Buzz";
            else $result[] = (String) $i;
        }
        return $result;
    }
}