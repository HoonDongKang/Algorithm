function solution(arr, query) {
    query.forEach((num, idx) => {
        arr = (idx % 2 === 0) ? arr.slice(0, num + 1) : arr.slice(num);
    });
    return arr;
}
