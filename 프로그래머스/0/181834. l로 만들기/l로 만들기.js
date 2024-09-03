function solution(myString) {
    return [...myString].map((char) => char.charCodeAt() <= 107 ? "l" : char).join("");
}
