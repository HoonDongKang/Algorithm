function solution(code) {
  let mode = 0;
  let res = [];
  const length = code.length;
  
  for (let i = 0; i < length; i++) {
    if (code[i] === '1') {
      mode = mode === 1 ? 0 : 1;
    } else {
      if ((mode === 0 && i % 2 === 0) || (mode === 1 && i % 2 === 1)) {
        res.push(code[i]);
      }
    }
  }
  
  return res.length ? res.join('') : 'EMPTY';
}