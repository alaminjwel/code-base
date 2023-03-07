<?php
//https://leetcode.com/problems/capitalize-the-title/description/
class Solution {

    /**
     * @param String $title
     * @return String
     */
      function wordPattern($pattern, $s) { {
        $word = explode(' ',$title);
        for($i=0;$i<count($word);$i++){
            $temp= strtolower($word[$i]);
            if(strlen($temp)>2) $temp = ucfirst($temp);
            $word[$i] = $temp;
        }
        return implode(' ',$word);
    }
}