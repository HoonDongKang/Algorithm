function solution(myString, pat) {
  let count = 0;
  for (let i = 0; i < myString.length - pat.length + 1; i++) {
    let str = [...myString];
    if (str.splice(i, pat.length).join('') === pat) count++;
  }

  return count;
}
