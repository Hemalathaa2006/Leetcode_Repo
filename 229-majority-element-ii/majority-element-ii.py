class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        frequencies = {}   

        for num in nums:
            if num in frequencies:
                frequencies[num] += 1  
            else:
                frequencies[num] = 1 

        max_elements = []
        
        for num, count in frequencies.items():
            if count > n//3:
                max_elements.append(num)
                
        return max_elements
