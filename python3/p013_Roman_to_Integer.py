"""
https://leetcode.com/problems/roman-to-integer/description/

Your runtime beats 91.02 % of python3 submissions.
"""
class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        s = s[::-1]
        result = 0
        last = 0
        for c in s:
            if dict[c] < last:
                result -= dict[c]
            else:
                result += dict[c]
            last = dict[c]

        return result