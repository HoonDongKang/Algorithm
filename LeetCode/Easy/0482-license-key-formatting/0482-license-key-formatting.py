class Solution:
    def licenseKeyFormatting(self, s: str, k: int):
        result = []
        s = "".join(s.split("-")).upper()
        while s:
            if len(s) >= k:
                result.append(s[-k:])
                s = s[0:-k]
            else:
                result.append(s)
                s = ""

        return "-".join(result[::-1])
        