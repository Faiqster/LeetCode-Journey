class Solution(object):
    def longestCommonPrefix(self, strs):
      min=len(strs[0])
      for i in strs:
        if len(i)<min:
          min=len(i)
      prefix=""
      for i in range(min):
        match=strs[0][i]
        for j in range(len(strs)):
          if strs[j][i]==match:
            match=strs[j][i]
          else:
            return prefix
        prefix=prefix+match
      return prefix