function solution(common) {
  const [x1, x2, x3, ...arg] = common;

  const diff = x2 - x1;
  const diff2 = x3 - x2;

  const diff3 = x2 / x1;

  if (diff === diff2) return common[common.length - 1] + diff;
  return common[common.length - 1] * diff3;
}
