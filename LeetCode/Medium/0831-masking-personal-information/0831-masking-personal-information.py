class Solution:
    def maskPII(self, s: str) -> str:
        if '@' in s:
            name, domain = s.split('@')
            return name[0].lower() + '*****' + name[-1].lower() + '@' + domain.lower()
        
        # 숫자만 추출
        digits = [c for c in s if c.isdigit()]
        local = "***-***-" + "".join(digits[-4:])
        
        if len(digits) == 10:
            return local
        
        country = '+' + '*' * (len(digits) - 10) + '-'
        return country + local