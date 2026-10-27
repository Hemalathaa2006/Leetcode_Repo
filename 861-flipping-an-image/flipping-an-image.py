class Solution(object):
    def flipAndInvertImage(self, image):
        """
        :type image: List[List[int]]
        :rtype: List[List[int]]
        """
        for row in image:
            row.reverse()
        
        for row in image:
            for i in range(len(row)):
                if row[i]==0:
                    row[i]=1
                else:
                    row[i]=0
        return image

        