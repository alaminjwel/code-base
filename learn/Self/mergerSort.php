<?php
class Solution {
    function mergeSort($array) {
        $count = count($array);

        // An array with one value is sorted
        if($count<2) return $array; 

        // Split array in half
        $mid = ceil($count/2);
        $left = $right = [];
        for($i=0;$i<$mid;$i++){
            $left[] = $array[$i];
        }
        for($i=$mid;$i<$count;$i++){
            $right[] = $array[$i];
        }
        // Sort half, recursively
        $left = $this->mergeSort($left);
        $right = $this->mergeSort($right);

        // Now merge the two sorted halves together, in a sorted manner
        return $this->merge($left,$right);
    }
    function merge($left,$right){

        $lc = count($left);
        $rc = count($right);
        $l = $r = 0;
        $merged= [];
        while($l<$lc && $r<$rc){
            if($left[$l]<=$right[$r]){
                $merged[] = $left[$l];
                $l++;
            }
            else{
                $merged[] = $right[$r];
                $r++;    
            }
        }

        // A good chance we will be left over with one array still having more values because left and right part may not equal
        while($l<$lc){
            $merged[] = $left[$l];
            $l++;
        }
        while($r<$rc){
            $merged[] = $right[$r];
            $r++;
        }
        return $merged;

    }
}
$obj = new Solution;
echo '<pre>';
print_r($obj->mergeSort([1,4,7,2,9,0,5]));
