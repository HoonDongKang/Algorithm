function solution(n) {
    return Array.from({length: n + 1}, (_, index) => index).filter((number) => number % 2 ===1);
}