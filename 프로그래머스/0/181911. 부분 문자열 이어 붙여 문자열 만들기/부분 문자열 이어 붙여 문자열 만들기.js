function solution(my_strings, parts) {
  let answer = [];
  my_strings.forEach((string, index) => {
    answer.push(
      [...string].slice(parts[index][0], parts[index][1] + 1).join('')
    );
  });

  return answer.join('');
}