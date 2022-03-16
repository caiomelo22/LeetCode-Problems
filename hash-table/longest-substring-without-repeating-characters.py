# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 22:43:16 2022

@author: caiog

Problem: https://leetcode.com/problems/longest-substring-without-repeating-characters/
"""

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        used = dict()
        last_non_duplicate = 0
        biggest = 0
        
        for i in range(len(s)):
            if s[i] in used:
                last_non_duplicate = max(used[s[i]] + 1, last_non_duplicate)
                
            biggest = max(i-last_non_duplicate+1, biggest)
            used[s[i]] = i
            
        return biggest
        