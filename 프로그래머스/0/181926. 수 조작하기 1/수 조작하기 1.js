function solution(n, control) {
    var answer = n;
    [...control].forEach((char) => {
        if (char === 'w') {
            answer += 1;
        } else if (char === 's') {
            answer -= 1;
        } else if (char === 'd') {
            answer += 10;
        } else if (char === 'a') {
            answer -= 10;
        }
    });
    return answer;
}