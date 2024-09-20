const checkArr = (arr1, arr2) => {
    return JSON.stringify(arr1) === JSON.stringify(arr2);
}

const calc = (arr) => {
    return arr.map((num) => {
        if(num >= 50 && num % 2 === 0) return num /= 2;
        if(num < 50 && num % 2 !== 0) return num = num * 2 + 1;
        else return num;
    });
}

function solution(arr) {
    let answer = 0;
    let arr2 = [];
    while(!checkArr(arr, arr2)){
        arr2 = [...arr];
        arr = calc(arr);
        answer++;
    }
    return answer - 1;
}
