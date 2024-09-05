function solution(myString) {
    var answer = [];
    for(let arr of myString.split("x")){
        answer.push(arr.length)
    }
    
    return answer;
}