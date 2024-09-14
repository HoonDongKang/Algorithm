function solution(my_string, s, e) {
    let input = [...my_string];
    let reversed = input.slice(s, e + 1).reverse();
    input.splice(s, e - s + 1, ...reversed);
    return input.join("");
}
