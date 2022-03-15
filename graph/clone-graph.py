# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 22:54:54 2022

@author: caiog

Problem: https://leetcode.com/problems/clone-graph/
"""

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        