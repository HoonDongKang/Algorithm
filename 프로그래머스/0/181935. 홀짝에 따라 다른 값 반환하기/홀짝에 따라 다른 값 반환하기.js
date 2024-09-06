const getArr = (n, type) => {
    let arr = [];
    let count = 1;
    while(count <= n){
        if(type === "odd" && count % 2 === 1) arr.push(count);
        if(type === "even" && count % 2 === 0) arr.push(count);
        count ++
    }
    
    return arr;
}

function solution(n) {
    if(n % 2 === 0) {
        return getArr(n, "even").reduce((acc, cur) => acc+=cur ** 2, 0)
    } else return getArr(n, "odd").reduce((acc, cur) => acc+=cur, 0)
}