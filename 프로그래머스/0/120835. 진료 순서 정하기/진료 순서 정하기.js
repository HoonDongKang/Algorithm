function solution(emergency) {
  let sorted = [...emergency].sort((a, b) => b - a);

  return emergency.map((value) => sorted.indexOf(value) + 1);
}