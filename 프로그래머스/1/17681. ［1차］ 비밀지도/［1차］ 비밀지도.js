function solution(n, arr1, arr2) {
  let map = Array.from({ length: n }, () => Array(n).fill(' '));
  arr1.forEach((el, i) => {
    let a = el.toString(2).padStart(n, '0');
    let b = arr2[i].toString(2).padStart(n, '0');

    [...a].forEach((e, j) => {
      if (e === '1' || b[j] === '1') {
        map[i][j] = '#';
      } else {
        map[i][j] = ' ';
      }
    });
  });
  return map.map((row) => row.join(''));
}