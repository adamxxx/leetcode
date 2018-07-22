#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
lins: https://leetcode.com/problems/two-sum/
notes:
1. this's time complexity O(n^2), but space complexity O(1) solution
2. can apply the hash table to reduce the time complexity O(n), but the space will be increaed to (n)
"""

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i, n1 in enumerate(nums):
            for j, n2 in enumerate(nums):
                if ((n1 + n2) == target and (i != j)):
                    return [i, j]
        return []
