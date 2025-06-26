function insert(intervals: number[][], newInterval: number[]): number[][] {
    const result: number[][] = [];

    let idx = 0;

    while (idx < intervals.length && intervals[idx][1] < newInterval[0]) {
        result.push(intervals[idx]);
        idx++;
    }

    while (idx < intervals.length && intervals[idx][0] <= newInterval[1]) {
        newInterval = [
            Math.min(intervals[idx][0], newInterval[0]),
            Math.max(intervals[idx][1], newInterval[1]),
        ];
        idx++;
    }

    result.push(newInterval);

    while (idx < intervals.length) {
        result.push(intervals[idx]);
        idx++;
    }

    return result;
};