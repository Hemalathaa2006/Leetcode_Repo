class Solution(object):
    def sumOfGoodNumbers(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        total = 0
        n= len(nums)

        for i in range(n):
            if i >= k and nums[i] <= nums[i - k]:
                continue
            if i + k < n and nums[i] <= nums[i + k]:
                continue
            total += nums[i]

        return total
        