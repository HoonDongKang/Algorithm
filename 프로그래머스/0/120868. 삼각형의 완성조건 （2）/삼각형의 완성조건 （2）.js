function solution(sides) {
  const max = Math.max(...sides);
  const min = Math.min(...sides);
  const lower = max - (max - min);
  const upper = max + min - 1 - max;
  return lower + upper;
}