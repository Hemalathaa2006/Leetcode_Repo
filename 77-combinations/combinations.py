class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        result = []
        
        def build_basket(start, basket):
            if len(basket)==k:
                result.append(list(basket))
                return
            for i in range(start, n+1):
                basket.append(i)

                build_basket(i+1,basket)
                basket.pop()

        build_basket(1,[])
        return result