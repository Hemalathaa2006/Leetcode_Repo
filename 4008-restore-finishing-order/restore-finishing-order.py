class Solution(object):
    def recoverOrder(self, order, friends):
        """
        :type order: List[int]
        :type friends: List[int]
        :rtype: List[int]
        """
        s = []
        for i in order:
            if i in friends:
                s.append(i)
        return s
        