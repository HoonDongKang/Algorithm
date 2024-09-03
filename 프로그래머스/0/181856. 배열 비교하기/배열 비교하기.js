function solution(arr1, arr2) {
    const winner = ""
    if(arr1.length > arr2.length) return 1;
    if(arr1.length < arr2.length) return -1;
    if(arr1.length === arr2.length) {
        const sum1 = arr1.reduce((acc, cur) => acc += cur, 0);
        const sum2 = arr2.reduce((acc, cur) => acc += cur, 0);
        if(sum1 > sum2) return 1;
        if(sum2 > sum1) return -1
    }
    return 0
}