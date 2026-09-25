class Solution(object):
    def isPossibleToSplit(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        counts = {}
        
        for num in nums:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1
            if counts[num] > 2:
                return False
        return True

        