function solution(arr, n) {
    return arr.map((value, index) => {
        if (arr.length % 2 !== 0 && index % 2 === 0) {
            return value + n;
        } else if (arr.length % 2 === 0 && index % 2 !== 0) {
            return value + n;
        }
        return value;
    });
}