function solution(num_list, n) {
  let front = num_list.splice(0, n);
  return [...num_list, ...front];
}