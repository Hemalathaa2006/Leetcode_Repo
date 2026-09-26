class Solution(object):
    def getCommon(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        n = len(nums1)
        m = len(nums2)
        i = 0
        j = 0

        while i < n and j < m:
            if nums1[i] == nums2[j]:
                return nums1[i]  
            elif nums1[i] < nums2[j]:
                i += 1          
            else:
                j += 1           
                
        return -1 
        