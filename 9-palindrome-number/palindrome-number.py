class Solution(object):
    def isPalindrome(self, x):
        x=str(x)
        y=x[::-1]
        return True if x==y else False
        