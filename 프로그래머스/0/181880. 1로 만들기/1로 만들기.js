const division = (num) => {
    return num % 2 === 0 ? num / 2 : (num - 1) / 2;
}

function solution(num_list) {
    var answer = 0;
    num_list.forEach((num) => {
        while(num !== 1) {
            num = division(num);
            answer ++;
        }
    })
    
    return answer;
}