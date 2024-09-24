const isPrime= (n) => {
    if (n <= 1) return false;
    if (n === 2) return true;
    if (n % 2 === 0) return false;
    for (let i = 3; i <= Math.sqrt(n); i += 2) {
        if (n % i === 0) return false;
    }
    return true;
}

function solution(n, k) {
    const base = n.toString(k);
    const candidates = base.split("0").filter((n) => n);
    let result = 0;
    for(let candidate of candidates) {
        if(isPrime(+candidate)) result ++;
    }
    
    return result;
}