function solution(array) {
  let count = 0;
  for (let num of array) {
    [...(num + '')].forEach((char) => {
      if (char === '7') count++;
    });
  }

  return count;
}