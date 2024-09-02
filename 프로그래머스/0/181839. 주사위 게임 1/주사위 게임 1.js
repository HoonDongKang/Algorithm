const isOdd = (num) => num % 2 !== 0;

function solution(a, b) {
    if(isOdd(a) && isOdd(b)) return a**2 + b**2;
    if(isOdd(a) || isOdd(b)) return 2 * (a + b);
    else return Math.abs(a-b)
}