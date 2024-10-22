function solution(n, words) {
  let result = [0, 0];

  for (let i = 1; i < words.length; i++) {
    if (
      words.indexOf(words[i]) !== i ||
      words[i - 1].slice(-1) !== words[i][0]
    ) {
      let turn = Math.floor(i / n) + 1;
      let person = (i % n) + 1;
      return [person, turn];
    }
  }

  return result;
}