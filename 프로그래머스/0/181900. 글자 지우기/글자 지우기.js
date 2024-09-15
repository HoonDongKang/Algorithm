function solution(my_string, indices) {
    indices.sort((a, b) => a - b);
    return [...my_string].filter((_, i) => !indices.includes(i)).join("");
}