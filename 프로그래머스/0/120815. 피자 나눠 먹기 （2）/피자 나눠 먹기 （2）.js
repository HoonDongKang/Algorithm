const getGCD = (num1, num2) => {
    let r = 0;
    while (num2 !== 0) {
        r = num1 % num2;
        num1 = num2;
        num2 = r;
    }
    return num1;
}

const getLCM = (num1, num2) => {
    return (num1 * num2) / getGCD(num1, num2);
}

function solution(n) {
    return getLCM(n, 6) / 6;
}