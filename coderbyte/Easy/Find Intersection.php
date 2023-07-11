<?php 
function FindIntersection($strArr) {
    $arr1 = explode(", ", $strArr[0]);
    $arr2 = explode(", ", $strArr[1]);    
    $intersection = array_intersect($arr1, $arr2);    
    if (count($intersection) == 0){
        return "false";
    }    
    return implode(",", $intersection);
}
   
// keep this function call here  
echo FindIntersection(array("1, 5, 6, 7, 10, 11, 12", "5, 6, 8, 11, 17"));  

?>