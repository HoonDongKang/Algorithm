function solution(k, score) {
    let hallOfFame = [];
    let result = [];

    score.forEach(s => {
        hallOfFame.push(s);
        hallOfFame.sort((a, b) => b - a);
        
        if (hallOfFame.length > k) {
            hallOfFame.pop();
        }
        
        result.push(hallOfFame[hallOfFame.length - 1]);
    });

    return result;
}
