class Solution(object):
    def commonFactors(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        fac = set()
        for i in range(1,a+1):
            if a%i==0:
                fac.add(i)
                
        count = 0
        for j in range(1,b+1):
            if b%j==0:
                if j in fac:
                    count += 1

        return count
       
        