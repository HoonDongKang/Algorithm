function solution(a, b) {
    return a.map((num, i) => num * b[i]).reduce((acc,cur) => acc+=cur, 0)
}