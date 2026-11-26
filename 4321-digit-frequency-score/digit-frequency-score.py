class Solution(object):
    def digitFrequencyScore(self, n):
        """
        :type n: int
        :rtype: int
        """
        score = 0

        while n >0:
            digit = n % 10
            score += digit
            n //= 10
        return score
        