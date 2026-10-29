class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        # arr.sort()
        # occur = []
        # i = 0
        # while i<len(arr):
        #     cnt = 1
        #     while i+1 <len(arr) and arr[i] == arr[i+1]:
        #         cnt += 1
        #     occur.append(cnt)

        # occur.sort()
        # for i in range(1,len(v)):
        #     if occur[i]==occur[i-1]:
        #         return False
        # return True

        counts = {}
        for num in arr:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1
                
        seen_counts = set()
        for freq in counts.values():
            if freq in seen_counts:
                return False
            seen_counts.add(freq)
            
        return True 

        