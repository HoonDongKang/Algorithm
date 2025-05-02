function wordBreak(s: string, wordDict: string[]): boolean {
    const wordSet = new Set(wordDict);
    const dp = new Array(s.length + 1).fill(false);
    dp[0] = true;

    for (let end = 1; end <= s.length; end++) {
        for (let start = 0; start < end; start++) {
            const isExists = wordSet.has(s.slice(start, end));
            if (isExists && dp[start]) {
                dp[end] = true;
                break;
            }
        }
    }
    return dp[s.length];
};