class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dict = {'(': ')', '{': '}', '[': ']'}
        stack = []
        for c in s:
            if stack != [] and dict.get(stack[-1]) and dict[stack[-1]] == c:
                stack.pop()
            else:
                stack.append(c)
        return stack == []


print(Solution().isValid("([)]"))
print(Solution().isValid("()[]{}"))