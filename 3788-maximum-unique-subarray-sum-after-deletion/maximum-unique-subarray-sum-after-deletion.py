class Solution(object):
    def maxSum(self,nums):
        i=0
        negatives=[]
        while i<len(nums):
            if len(nums)==1 and negatives==[]:
                break
            if nums.count(nums[i])>1:
                nums.remove(nums[i])
                i=0
            elif nums[i]<0:
                negatives.append(nums[i])
                nums.remove(nums[i])
                i=0
            else:
                i+=1
        if nums==[]:
            return max(negatives)

        return sum(nums)
