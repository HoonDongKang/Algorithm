function solution(hp) {
  const first = Math.floor(hp / 5);
  const second = Math.floor((hp - first * 5) / 3);
  const third = Math.floor((hp - first * 5 - second * 3) / 1);

  return first + second + third;
}