function getGCD(a, b) {
    while (b !== 0) {
        const temp = b;
        b = a % b;
        a = temp;
    }
    return a;
}

function getLCM(num1, num2) {
    return (num1 * num2) / getGCD(num1, num2);
}

function solution(numer1, denom1, numer2, denom2) {
    const lcm = getLCM(denom1, denom2);
    const combinedNumer = (lcm / denom1 * numer1) + (lcm / denom2 * numer2);
    const gcd = getGCD(combinedNumer, lcm);
    
    return [combinedNumer / gcd, lcm / gcd];
}