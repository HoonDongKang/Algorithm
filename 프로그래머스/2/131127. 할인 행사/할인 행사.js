function solution(want, number, discount) {
  let count = 0;

  const wantObj = {};
  want.forEach((item, i) => {
    wantObj[item] = number[i];
  });
  for (let i = 0; i <= discount.length - 10; i++) {
    const obj = {};

    for (let j = i; j < i + 10; j++) {
      const item = discount[j];
      obj[item] = (obj[item] || 0) + 1;
    }

    let valid = true;
    for (const item in wantObj) {
      if (obj[item] !== wantObj[item]) {
        valid = false;
        break;
      }
    }

    if (valid) count++;
  }

  return count;
}