function longestCommonPrefix(strs: string[]): string {
    if (!strs.length) return "";
    
    let minLen = Math.min(...strs.map(s => s.length));
    
    let low = 1, high = minLen;
    
    const isCommonPrefix = (length: number): boolean => {
        const prefix = strs[0].substring(0, length);
        return strs.every(s => s.startsWith(prefix));
    };

    while (low <= high) {
        let mid = Math.floor((low + high) / 2);
        if (isCommonPrefix(mid)) {
            low = mid + 1;
        } else {
            high = mid - 1;
        }
    }
    
    return strs[0].substring(0, (low + high) / 2);
}
