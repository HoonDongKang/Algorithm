function solution(my_string, queries) {
    let arr= [...my_string]
    queries.forEach(([x, y]) => {
        let cut = arr.slice(x, y + 1).reverse();
        arr.splice(x, y -x +1, ...cut);
        
    })
    return arr.join("")
}