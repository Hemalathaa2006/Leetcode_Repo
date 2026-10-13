class Solution(object):
    def findGCD(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mini = min(nums)
        maxi = max(nums)

        ans = 1

        for i in range(1, maxi+1):
            if mini%i==0 and maxi%i==0:
                ans = i
        return ans
        