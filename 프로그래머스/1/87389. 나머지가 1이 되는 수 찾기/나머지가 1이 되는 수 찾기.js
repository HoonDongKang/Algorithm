function solution(n) {
    let num = n - 1
    const arr = [];
    let count = 0;
    while( count <= num ) {
        if(num % count === 0) arr.push(count);
        count++
    }
    
    console.log(arr)
    return arr[1]
}