class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        count = 0
        n = len(heights)
        expected = sorted(heights)
        for i in range(0,n):
            if heights[i] != expected[i]:
                count += 1
        return count
        