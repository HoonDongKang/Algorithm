function solution(picture, k) {
  let result = [];
  picture.forEach((str) => {
    let changed = [...str].map((char) => char.repeat(k)).join('');
    for (let i = 0; i < k; i++) {
      result.push(changed);
    }
  });

  return result;
}