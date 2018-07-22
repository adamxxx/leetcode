#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
link: https://leetcode.com/problems/reverse-integer/
notes:
1. for 2**31 condition, int class has a bit_length() function
'''

class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        negative = x < 0
        x_str = str(x)
        if(negative):
            x_str=x_str[1:]
        x_list = list(x_str)
        x_list.reverse()

        # int('01234') => '1234'
        x_result = int(''.join(x_list))
        
        if(negative):
            x_result = x_result * -1
        
        # handle the case for 32-bit signed integer
        if (-2**31 > x_result or x_result > 2**31-1):
            return 0

        return x_result
            
        