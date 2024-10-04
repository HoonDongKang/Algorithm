function solution(s) {
    let arr = s.split(" ");
    return arr.map((word) => [...word].map((char,i) => {
        return i % 2 === 0 ? char.toUpperCase() : char.toLowerCase()
    }).join("")).join(" ")
}