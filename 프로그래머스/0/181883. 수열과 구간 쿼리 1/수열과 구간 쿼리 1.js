function solution(arr, queries) {
    queries.forEach(([x, y]) => arr.map((num, i) => {
        if(x <= i && i<= y) arr[i] ++
    }))
    return arr
}