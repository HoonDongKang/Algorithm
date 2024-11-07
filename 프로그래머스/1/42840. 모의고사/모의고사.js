function solution(answers) {
    const patterns = [
        [1, 2, 3, 4, 5],
        [2, 1, 2, 3, 2, 4, 2, 5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ];
    
    const scores = [0, 0, 0];
    
    answers.forEach((answer, i) => {
        patterns.forEach((pattern, index) => {
            if (answer === pattern[i % pattern.length]) {
                scores[index]++;
            }
        });
    });

    const maxScore = Math.max(...scores);
    
    return scores
        .map((score, index) => (score === maxScore ? index + 1 : null))
        .filter(num => num !== null);
}
