<?php
//https://www.youtube.com/watch?v=NrHpgTScOcY
class Solution {
    /**
     * @param String[] $ideas
     * @return Integer
     */
    function distinctNames($ideas) {
        $groups = [];
        foreach ($ideas as $idea) {
           $prefix = substr($idea,0,1);
           $groups[$prefix][] = substr($idea,1,strlen($idea)-1);
        }
        $res= 0 ;
        foreach($groups as $prefix1=>$group1){
           foreach($groups as $prefix2=>$group2){
              if($prefix1 == $prefix2) continue;
              $intersect = count(array_intersect($group1, $group2));
              $distinct1 = count($group1) - $intersect;
              $distinct2 = count($group2) - $intersect;
              $res += $distinct1 * $distinct2;              
           }
        }

        return $res;       
    }
}