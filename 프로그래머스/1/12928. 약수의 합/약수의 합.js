function solution(n) {
    let count = 0;
    const arr = [];
    while(count <= n){
        if(n % count === 0) arr.push(count);
        count ++;
    }
    
    return arr.reduce((acc, cur) => acc += cur, 0);
}