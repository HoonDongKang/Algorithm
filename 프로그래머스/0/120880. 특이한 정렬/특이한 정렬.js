function solution(numlist, n) {
  var answer = [];
  let sorted = numlist
    .map((num, index) => {
      return { num, diff: Math.abs(num - n), index };
    })
    .sort((a, b) => {
      if (a.diff === b.diff) return b.num - a.num;
      return a.diff - b.diff;
    });

  return sorted.map(({ num }) => num);
}