function solution(arr, flag) {
  let result = [];
  flag.forEach((f, i) => {
    if (f) {
      result = [...result, ...Array.from({ length: arr[i] * 2 }).fill(arr[i])];
    } else {
      result.splice(result.length - arr[i]);
    }
  });
  return result;
}