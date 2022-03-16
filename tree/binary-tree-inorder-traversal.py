# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 22:41:42 2022

@author: caiog

Problem: https://leetcode.com/problems/binary-tree-inorder-traversal/
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return []
        
        return_list = []
        if root.left != None:
            return_list.extend(self.inorderTraversal(root.left))
        return_list.extend([root.val])
        if root.right != None:
            return_list.extend(self.inorderTraversal(root.right))
        return return_list