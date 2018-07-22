"""
You are here! 
Your runtime beats 80.72 % of python3 submissions.
https://leetcode.com/problems/longest-common-prefix/
"""
class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if(strs == []):
            return ''

        lcp = ''
        for x in range(0, len(strs[0])):
            flag = True
            _lcp = lcp
            _lcp+=strs[0][x]
            for i in range(0, len(strs)):
                if not strs[i].startswith(_lcp):
                    flag = False
            if flag:
                lcp=_lcp
            else:
                break
        return lcp


# print(Solution().longestCommonPrefix(["c","acc","ccc"]))
# print(Solution().longestCommonPrefix(["flower","flow","flight"]))
# print(Solution().longestCommonPrefix([]))
# print(Solution().longestCommonPrefix(['a']))