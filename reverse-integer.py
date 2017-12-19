'''
Problem:

Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output:  321

Example 2:

Input: -123
Output: -321

Example 3:

Input: 120
Output: 21

Note:
Assume we are dealing with an environment which could only hold integers within the 32-bit signed integer range.
For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
'''

'''

'''

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        s = str(x)
        print s
        if s[0] == '-':
            xRev = int('-' + s[len(s):0:-1])
            if xRev > 2147483647 or xRev < -2147483648:
                return 0
            else:
                return xRev
        else:
            xRev = int(s[::-1])
            if xRev > 2147483647 or xRev < -2147483648:
                return 0
            else:
                return xRev

    def reverseFaster(self, x):
        """
        :type x: int
        :rtype: int
        """
        res = 0
        sign = 1
        num = []

        if x < 0:
            sign = -1
        if x == 0:
            return 0
        x = abs(x)

        while x:
            num.append(x%10)
            x //= 10

        for i in num:
            res *= 10
            res += i

        if res > 0x7FffFFff:
            return 0
        else:
            return res * sign

myClass = Solution()
print myClass.reverse(-12345678)
print myClass.reverse(-2147483648)
print myClass.reverseFaster(-12345678)
print myClass.reverseFaster(-2147483648)