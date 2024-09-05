function solution(numLog) {
    let answer = "";
    numLog.forEach((num, i) => {
    switch(numLog[i+1] - num) {
        case 1:
            answer += "w"
            break;
        case -1:
            answer += "s"
            break;
        case 10:
            answer += "d";
            break;
        case -10:
            answer += "a";
            break;
    }} )
    return answer
}