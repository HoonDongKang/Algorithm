function solution(A, B) {
  let strings = [A];

  let word = [...A];
  for (let i = 0; i < word.length; i++) {
    let lastChar = word.pop();
    word = [lastChar, ...word];
    strings.push(word.join(''));
  }

  return strings.includes(B) ? strings.indexOf(B) : -1;
}