function solution(s) {
  const result = [];
  const lastIndex = {};

  for (let i = 0; i < s.length; i++) {
    const char = s[i];

    if (lastIndex[char] !== undefined) {
      result.push(i - lastIndex[char]);
    } else {
      result.push(-1);
    }

    lastIndex[char] = i;
  }

  return result;
}