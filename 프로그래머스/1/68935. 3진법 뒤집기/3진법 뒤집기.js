function solution(n) {
    const reversedTernary = n.toString(3).split("").reverse().join("");
    
    return parseInt(reversedTernary, 3);
}