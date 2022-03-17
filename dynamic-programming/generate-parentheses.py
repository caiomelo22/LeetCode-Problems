# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 22:43:50 2022

@author: caiog

Problem: https://leetcode.com/problems/generate-parentheses/
"""

class Solution(object):
    def generate_parenthesis_aux(self, left, right, path, return_list):
        if left < 0 or right < 0:
            return None
        
        if left > right:
            return None
        
        if left == 0 and right == 0:
            return_list.append(path)
        
        self.generate_parenthesis_aux(left - 1, right, path + '(', return_list)
        self.generate_parenthesis_aux(left, right - 1, path + ')', return_list)
        
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        return_list = []
        path = ''
        self.generate_parenthesis_aux(n, n, path, return_list)
        
        return return_list