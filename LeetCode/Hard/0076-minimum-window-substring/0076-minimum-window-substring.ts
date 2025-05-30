function minWindow(s: string, t: string): string {
    const map = new Map<string, number>();
    let required = t.length;
    let left = 0;
    let minLen = Infinity;
    let minStart = 0;

    for (const char of t) {
        map.set(char, (map.get(char) || 0) + 1);
    }

    for (let right = 0; right < s.length; right++) {
        const char = s[right];

        if (map.has(char)) {
            const count = map.get(char)!;
            if (0 < count) required--;
            map.set(char, count - 1);
        }

        while (required === 0) {
            const char = s[left];

            if (right - left + 1 < minLen) {
                minLen = right - left + 1;
                minStart = left;
            }

            if (map.has(char)) {
                map.set(char, map.get(char)! + 1);
                if (map.get(char)! > 0) {
                    required++;
                }
            }
            left++;
        }
    }
    return minLen === Infinity ? "" : s.slice(minStart, minStart + minLen);
}
