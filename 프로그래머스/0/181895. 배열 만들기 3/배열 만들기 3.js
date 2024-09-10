function solution(arr, intervals) {
    return intervals.reduce((result, ar) => result.concat(arr.slice(ar[0], ar[1] + 1)), []);
}
