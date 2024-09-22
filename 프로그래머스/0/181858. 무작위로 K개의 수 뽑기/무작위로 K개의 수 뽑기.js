function solution(arr, k) {
  let a = Array.from(new Set(arr));

  if (a.length < k) {
    return [...a, ...Array.from({ length: k - a.length }).fill(-1)];
  }

  return a.slice(0, k);
}
