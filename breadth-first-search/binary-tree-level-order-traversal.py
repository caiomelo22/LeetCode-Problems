# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 22:49:05 2022

@author: caiog

Problem: https://leetcode.com/problems/binary-tree-level-order-traversal/
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None:
            return []
        
        queue = []     #Initialize a queue
        
        queue.append(root)
        return_list = []

        while queue:          # Creating loop to visit each node
            
            append_value = []
            len_current_level = len(queue)
            
            for i in range(len_current_level):
                node = queue.pop(0) 
                append_value.append(node.val)

                if node.left != None:
                    queue.append(node.left)

                if node.right != None:
                    queue.append(node.right)

            if len(append_value) > 0:
                return_list.append(append_value)
        
        return return_list
        