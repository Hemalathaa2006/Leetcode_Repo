class Solution(object):
    def maxPower(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
            
        maxi = 1
        count = 1
        
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                count += 1
            else:
                maxi = max(maxi, count)
                count = 1
                
        return max(maxi, count)

        