function solution(n) {
    return Array.from({length: n}, (v,i) => {
        return i % 2 === 0 ? "수" : "박"
    }).join("")
}