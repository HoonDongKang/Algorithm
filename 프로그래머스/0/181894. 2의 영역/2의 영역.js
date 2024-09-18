function solution(arr) {
    let idx = []
    arr.forEach((num,i)=> { if(num ===2) idx.push(i)})
    if(!idx.length) return [-1]
    return arr.slice(idx[0], idx[idx.length - 1] + 1);
}