function solution(arr) {
    let array = [];
    arr.forEach((num) => {
        array = [...array,Array.from({length: num}).fill(num)].flat()
    })
    return array;
}