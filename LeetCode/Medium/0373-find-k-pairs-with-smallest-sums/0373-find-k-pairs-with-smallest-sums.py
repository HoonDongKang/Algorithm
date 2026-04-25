import heapq
class Solution:
    def kSmallestPairs(self, nums1: list[int], nums2: list[int], k: int) -> list[list[int]]:
        heap = [(nums1[0]+ nums2[0], 0,0)]
        visited = {(0, 0)}

        result = []

        heapq.heapify(heap)
        while heap and k:
            sum, a, b= heapq.heappop(heap)
            result.append((nums1[a], nums2[b]))

            next_index1 = a+1
            next_index2 = b+1

            if next_index1 < len(nums1) and (next_index1, b) not in visited:
                visited.add((next_index1, b))
                heapq.heappush(heap, (nums1[next_index1]+nums2[b],next_index1, b))

            if next_index2 < len(nums2) and (a, next_index2) not in visited:
                visited.add((a, next_index2))
                heapq.heappush(heap, (nums1[a]+nums2[next_index2],a, next_index2))
            
            k -=1


        return result