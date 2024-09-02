function solution(myString, pat) {
  return +([...myString]
    .map((char) => {
      if (char === 'A') return 'B';
      if (char === 'B') return 'A';
    })
    .join('')
    .includes(pat));
}
