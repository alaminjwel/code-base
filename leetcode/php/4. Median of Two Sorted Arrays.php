<?php

/*https://leetcode.com/problems/median-of-two-sorted-arrays*/

class Solution {

    /**
     * @param Integer[] $nums1
     * @param Integer[] $nums2
     * @return Float
     */
    function findMedianSortedArrays($nums1, $nums2) {        
        
        if(empty($nums1)) $finalNum = $nums2;
        else if(empty($nums2)) $finalNum = $nums1;
        else{
            $finalNum =  array_merge($nums1, $nums2);
            sort($finalNum);
        }
                
        $count = count($finalNum);
        
        if($count==1) $output = $finalNum[0];
        else if($count==2) $output = ($finalNum[0]+$finalNum[1])/2;
        else if($count==3) $output = $finalNum[1];
        else if($count%2==0){
        	$firstPos = ($count/2)-1;
            $secondPos = $firstPos+1;
            $output = ($finalNum[$firstPos]+$finalNum[$secondPos])/2;
        }
        else{
        	$firstPos = ($count+1)/2;
            $output = $finalNum[$firstPos-1];
        }
        return $output;
        
    }
}