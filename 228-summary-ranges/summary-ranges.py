class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        result = []
        i,j = 0,0
        while i < len(nums):
            while j <len(nums)-1 and nums[j] == nums[j+1] -1:
                j += 1
            if i==j:
                result.append(str(nums[i]))
            else:
                result.append(str(nums[i]) + "->" + str(nums[j]))
            j += 1
            i = j
        return result        