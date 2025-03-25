class Solution(object):
    def sortPeople(self, names, heights):
        """
        :type names: List[str]
        :type heights: List[int]
        :rtype: List[str]
        """

        def quickSort(left, right):
            if left >= right: return
            pivot = heights[right]
            partitionIndex = left

            for i in range(left, right):
                if heights[i] > pivot:
                    heights[i], heights[partitionIndex] = heights[partitionIndex], heights[i]
                    names[i], names[partitionIndex] = names[partitionIndex], names[i]
                    partitionIndex += 1

            heights[partitionIndex], heights[right] = heights[right], heights[partitionIndex]
            names[partitionIndex], names[right] = names[right], names[partitionIndex]
            
            quickSort(left, partitionIndex - 1)
            quickSort(partitionIndex + 1, right)

        quickSort(0,len(heights)-1)

        return names