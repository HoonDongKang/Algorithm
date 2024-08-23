function solution(my_string) {
  return [...my_string]
    .filter((string) => !Number.isNaN(Number(string)))
    .reduce((acc, num) => acc + Number(num), 0);
}