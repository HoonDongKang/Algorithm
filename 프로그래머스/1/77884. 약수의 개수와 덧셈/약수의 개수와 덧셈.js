const getYak = (n) => {
    let count = 0;
    for (let i = 1; i * i <= n; i++) {
        if (n % i === 0) {
            count++;
            if (i !== n / i) {
                count++;
            }
        }
    }
    return count;
}

function solution(left, right) {
    return Array.from({ length: right - left + 1 }, (_, i) => i + left)
        .reduce((acc, cur) => {
            return getYak(cur) % 2 === 0
                ? acc + cur
                : acc - cur;
        }, 0);
}
