<?php
//https://leetcode.com/problems/convert-the-temperature/
class Solution {

    /**
     * @param Float $celsius
     * @return Float[]
     */
    function convertTemperature($celsius) {
        $k = $celsius + 273.15;
        $f =  ($celsius * 1.80) + 32.00;
        return [$k,$f];
    }
}