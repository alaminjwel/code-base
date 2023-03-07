<?php

class Solution {

    /**
     * @param String $num
     * @return Boolean
     */
    function digitCount($num) {
        $freq = [];
        for($i=0;$i<strlen($num);$i++){
            if(!isset($freq[$num[$i]])) $freq[$num[$i]] = 0;
            $freq[$num[$i]]++;
        }
        ksort($freq);
        for($i=0;$i<strlen($num);$i++){
            if(!isset($freq[$i])) $freq[$i] = 0;
            if($freq[$i]!=$num[$i]) return false;
        }
        return true;
    }
}