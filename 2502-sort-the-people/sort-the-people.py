class Solution(object):
    def sortPeople(self, names, heights):
        """
        :type names: List[str]
        :type heights: List[int]
        :rtype: List[str]
        """
        h = sorted(heights)
        h = h[::-1]
        result = []
        for i in h:
            result.append(names[heights.index(i)])
        return result
        