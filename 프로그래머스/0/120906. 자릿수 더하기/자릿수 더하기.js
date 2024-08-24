function solution(n) {
    return [...n.toString()].reduce((acc, num) => acc + (+num), 0)
}