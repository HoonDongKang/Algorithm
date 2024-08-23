function solution(cipher, code) {
  const multiples = Math.floor(cipher.length / code);
  let multipleArr = [];

  for (let i = 1; i < multiples + 1; i++) {
    multipleArr.push(code * i);
  }

  return multipleArr.map((i) => cipher[i - 1]).join('');
}