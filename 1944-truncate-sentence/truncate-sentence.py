class Solution(object):
    def truncateSentence(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """

        words = s.split()
        news = ""
        for i in range(k):
            news += words[i]
            if i != k-1:
                news += " "

        return news
        