function solution(A,B){
    let a = A.sort((a,b) => a - b);
    let b = B.sort((a,b) => b - a);

    return a.reduce((acc,cur,i) => acc += cur * b[i],0);
}