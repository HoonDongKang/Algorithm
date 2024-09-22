function solution(rank, attendance) {
    const validStudents = rank
        .map((score, index) => ({ score, index }))
        .filter(({ index }) => attendance[index])
        .sort((a, b) => a.score - b.score);
    const [first, second, third] = validStudents;

    return first.index * 10000 + second.index * 100 + third.index;
}