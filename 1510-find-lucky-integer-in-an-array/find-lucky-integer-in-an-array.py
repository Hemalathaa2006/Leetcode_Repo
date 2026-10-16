class Solution(object):
    def findLucky(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        count = Counter(arr)

        ans = -1

        for key, value in count.items():
            if key == value:
                ans = max(ans, key)
        
        return ans
        