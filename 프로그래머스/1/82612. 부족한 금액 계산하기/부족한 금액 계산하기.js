function solution(price, money, count) {
    let result = Array.from({length: count}, (_, i) => price * (i+1)).reduce((acc,cur) => acc+=cur, 0)
    
    return result > money ? result - money : 0
}