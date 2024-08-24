function solution(s1, s2) {
  let count = 0;

  s1.forEach(s1el => {
    if (s2.includes(s1el)) {
      count++;
    }
  });
  return count;
}