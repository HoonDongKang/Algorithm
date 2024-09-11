function solution(arr, queries) {
  queries.forEach((query) => {
    [arr[query[0]], arr[query[1]]] = [arr[query[1]], arr[query[0]]];
  });
  return arr;
}
