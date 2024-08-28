function solution(quiz) {
  let answer = [];
  quiz.forEach((item) => {
    let sequence = item.split('=');
    answer.push(eval(sequence[0].trim()) === +sequence[1].trim() ? 'O' : 'X');
  });
  return answer;
}