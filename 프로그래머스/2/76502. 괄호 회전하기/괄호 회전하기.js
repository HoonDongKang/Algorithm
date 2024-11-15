const isValid = (s) => {
  const stack = [];
  for (const char of s) {
    if (char === '(' || char === '[' || char === '{') {
      stack.push(char);
    } else {
      const last = stack.pop();
      if (
        (char === ')' && last !== '(') ||
        (char === ']' && last !== '[') ||
        (char === '}' && last !== '{')
      ) {
        return false;
      }
    }
  }
  return stack.length === 0;
};

function solution(s) {
  let answer = 0;
  const length = s.length;

  for (let i = 0; i < length; i++) {
    if (isValid(s)) answer++;
    s = s.slice(1) + s[0];
  }

  return answer;
}
