class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        result = []
        idx = 1
        for num in target:
            while idx < num:
                result.append('Push')
                result.append('Pop')
                idx += 1
            result.append('Push')
            idx += 1

        return result