function solution(a, b) {
    let min, max;
    if(a > b) {
        min = b;
        max = a;
    } else {
        min = a;
        max= b;
    }
    return Array.from({length: max - min + 1}, (_, i) => min + i).reduce((acc,cur) => acc+=cur, 0);
}