function solution(n) {
  const arr = Array.from({ length: n }, () => Array(n).fill(0));

  let num = 1;
  let rs = 0;
  let cs = 0;
  let re = n - 1;
  let ce = n - 1;

  while (rs <= re && cs <= ce) {
    for (let i = cs; i <= ce; i++) {
      arr[rs][i] = num++;
    }
    rs++;

    for (let i = rs; i <= re; i++) {
      arr[i][ce] = num++;
    }
    ce--;

    if (rs <= re) {
      for (let i = ce; i >= cs; i--) {
        arr[re][i] = num++;
      }
      re--;
    }

    if (cs <= ce) {
      for (let i = re; i >= rs; i--) {
        arr[i][cs] = num++;
      }
      cs++;
    }
  }

  return arr;
}