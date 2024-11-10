function solution(k, tangerine) {
  const sizeCount = {};
  tangerine.forEach((size) => {
    sizeCount[size] = (sizeCount[size] || 0) + 1;
  });

  const sortedCounts = Object.values(sizeCount).sort((a, b) => b - a);

  let selectedCount = 0;
  let types = 0;

  for (const count of sortedCounts) {
    selectedCount += count;
    types++;

    if (selectedCount >= k) break;
  }

  return types;
}
