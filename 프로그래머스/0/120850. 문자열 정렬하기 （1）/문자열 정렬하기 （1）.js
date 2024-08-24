function solution(my_string) {
  return [...my_string].filter((el) => !Number.isNaN(+el)).map((el) => +el).sort((a, b) => a-b);
}