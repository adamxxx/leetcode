class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        """
        x=12421
        step01: x=x/10 (1242), x/1/%10 (1)
        step02: x=x/10 (124), x/100/%10 (1*10 + 2=12)
        step02: x=x/10 (12), x/1000/%10 (12*10 + 4=124)
        
        notes: python2 123/10=12, py3 123/10=12.3
        """
        # approach 1: apply string, str(x)[::-1] == str(x)
        # approach 2(best): use number only, divide and mod
        
        # special case: negative number or last digit is zero
        if ( x < 0 or (x%10 == 0 and x != 0)):
            return False

        reversedNum = 0
        while (x > reversedNum):
            reversedNum = int(reversedNum * 10 + x%10)
            x=int(x/10)
        
        if(reversedNum == x or int(reversedNum/10) == x):
            return True
        
        return False

print(Solution().isPalindrome(12321))