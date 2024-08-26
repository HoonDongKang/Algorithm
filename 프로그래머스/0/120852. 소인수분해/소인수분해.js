function solution(n) {
    let arr = [];
    let count = 2;
    while (n > 1) {
        if (n % count === 0) {
            arr.push(count);
            n /= count;
        } else {
            count++;
        }
    }
    return Array.from(new Set(arr));
}