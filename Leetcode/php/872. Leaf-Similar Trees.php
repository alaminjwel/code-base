<?php
//https://leetcode.com/problems/leaf-similar-trees/
/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     public $val = null;
 *     public $left = null;
 *     public $right = null;
 *     function __construct($val = 0, $left = null, $right = null) {
 *         $this->val = $val;
 *         $this->left = $left;
 *         $this->right = $right;
 *     }
 * }
 */
class Solution {

    /**
     * @param TreeNode $root1
     * @param TreeNode $root2
     * @return Boolean
     */
    function leafSimilar($root1, $root2) {
        $v1 = [];
        $this->findLeaf($root1, $v1);
        $v2 = [];
        $this->findLeaf($root2, $v2);
        return $v1 == $v2;
    }

    function findLeaf($n,&$v){              
        if($n->left) $this->findLeaf($n->left,$v);
        if($n->right) $this->findLeaf($n->right,$v);
        if(!$n->left && !$n->right) $v[] = $n->val;
         
        return $v;
    }
}

$obj = new Solution;
echo '<pre>';
print_r($obj->leafSimilar([10,5,15,3,7,null,18],[10,5,15,3,7,null,18]));