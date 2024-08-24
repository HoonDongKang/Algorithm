function solution(n) {
    let index = 1;
    let arr = [];
    
    while (index <= n) {
        if(n % index === 0) arr.push(index);
        index ++;
    }
    
    return arr
}