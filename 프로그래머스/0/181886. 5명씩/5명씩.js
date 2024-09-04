function solution(names) {
    return names.filter((_, i) => i === 0 || i % 5 === 0)
}