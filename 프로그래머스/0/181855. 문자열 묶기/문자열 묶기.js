function solution(strArr) {
  let result = {};
  strArr.forEach((char) => {
    result[char.length] = result[char.length] ? result[char.length] + 1 : 1;
  });

  return Math.max(...Object.values(result));
}