const getEvenNumbers = (n) => {
    let numbers = [];
    while (n > 0) {
        if (n % 2 === 0) {
            numbers.push(n);
        }
        n--;
    }
    return numbers;
}

function solution(n) {
    const evenNumbers = getEvenNumbers(n);
    
    return evenNumbers.reduce((acc, num) => acc + num, 0);
}