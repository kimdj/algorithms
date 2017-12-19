'''
Problem:

Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Example:

Input: "cbbd"
Output: "bb"
'''

'''
Since a palindrome mirrors around its center, a palindrome can be expanded from its center.
There are only 2n-1 such centers because palindromes can have an even number of letters.

Time Complexity: O(n^2)
    Since expanding a palindrome around its center could take O(n), the overall complexity is O(n^2).
Space Complexity: O(1)
'''

class Solution(object):
    def longestPalindrome(self, s):
        start = 0
        end = 0
        for i in range(0, len(s)):
            len1 = Solution().expandAroundCenter(s, i, i)
            len2 = Solution().expandAroundCenter(s, i, i+1)
            lenMax = max(len1, len2)
            if lenMax > end - start:
                start = i - (lenMax - 1) / 2
                end = i + lenMax / 2
        return s[start:end+1]

    @staticmethod
    def expandAroundCenter(s, left, right):
        L = left
        R = right
        while (L >= 0 and R < len(s) and s[L] == s[R]):
            L -= 1
            R += 1
        return R - L - 1

myClass = Solution()
print "abcde ->", myClass.longestPalindrome("abcde")
print "babad ->", myClass.longestPalindrome("babad")
print "dbababadabababd ->", myClass.longestPalindrome("dbababadabababd")

