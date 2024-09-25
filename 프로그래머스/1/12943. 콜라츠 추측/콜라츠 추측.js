function solution(num) {
    for (let answer = 0; answer < 500; answer++) {
        if (num === 1) return answer;
        num = num % 2 === 0 ? num / 2 : num * 3 + 1;
    }
    return -1;
}
