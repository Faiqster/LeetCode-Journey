import numpy as np

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        num3 = nums1 + nums2
        num3 = np.sort(num3)  # Sort the combined list
        length = len(num3)
        
        # Check if the length is even or odd and return the median accordingly
        if length % 2 == 0:
            # Use float division to ensure the result is a float
            return (num3[length // 2 - 1] + num3[length // 2]) / 2.0
        else:
            return num3[length // 2]
