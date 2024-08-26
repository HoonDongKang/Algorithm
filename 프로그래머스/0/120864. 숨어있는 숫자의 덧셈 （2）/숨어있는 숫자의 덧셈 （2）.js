function solution(my_string) {
  return my_string.split(/[a-zA-Z]/g).reduce((acc, cur) => (acc += +cur), 0);
}