function solution(arr, queries) {
  let result = [];
  queries.forEach(([s, e, k]) => {
    let min = Infinity;
    for (let i = s; i <= e; i++) {
      if (arr[i] > k && arr[i] < min) {
        min = arr[i];
      }
    }
    if (min === Infinity) {
      result.push(-1);
    } else result.push(min);
  });

  return result;
}