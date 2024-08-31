function solution(my_string) {
  let answer = [];
  for (let i = 0; i < my_string.length; i++) {
    answer.push([...my_string].splice(i, my_string.length - i).join(''));
  }

  return answer.sort();
}
