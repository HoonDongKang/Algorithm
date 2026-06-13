class Solution:
    def restoreIpAddresses(self, s: str) -> list[str]:
        result = []

        def isValid(s) -> bool:
            if not s.isdigit():
                return False

            num = int(s)

            if num < 0 or num > 255:
                return False
            
            if s.startswith('0') and len(s) >= 2:
                return False
            
            return True
        
        def dfs(index, segments, seg_count):
            if seg_count == 4:
                if index == len(s):
                    result.append(".".join(segments))
                return
                    

            for end_idx in [1,2,3]:
                val = s[index: index + end_idx]
                if isValid(val):
                    segments.append(val)
                    dfs(index+end_idx, segments, seg_count + 1)
                    segments.pop()

        dfs(0,[], 0)

        return result
