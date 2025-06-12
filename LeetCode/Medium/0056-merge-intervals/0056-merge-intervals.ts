function merge(intervals: number[][]): number[][] {
    if (!intervals.length) return intervals;
    intervals.sort((a, b) => a[0] - b[0]);

    const result: number[][] = [intervals[0]];
    for (let i = 0; i < intervals.length; i++) {
        const prev = result[result.length - 1];
        const cur = intervals[i];

        if (cur[0] <= prev[1]) {
            prev[1] = Math.max(prev[1], cur[1]);
        } else {
            result.push(cur);
        }
    }

    return result;
};