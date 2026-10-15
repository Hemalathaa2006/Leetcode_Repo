class Solution(object):
    def alternatingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum = 0
        for i in range(0,len(nums)):
            if i%2==0:
                sum += nums[i]
            else:
                sum -= nums[i]
        return sum