class Solution(object):
    def longestPalindrome(self, s):
        length=len(s)
        long=''
        for i in range(length):
            sub=''
            for j in range(i,length):
                sub=sub+s[j]
                if sub==sub[::-1] and len(sub)>len(long):
                    long=sub
            if long==sub:
                return(long)
        return(long)