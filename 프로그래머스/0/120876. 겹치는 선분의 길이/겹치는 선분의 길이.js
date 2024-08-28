function solution(lines) {
  const commonLines = [];

  for (let i = 0; i < 3; i++) {
    const [x1, x2] = lines[i];
    for (let j = i + 1; j < 3; j++) {
      const [x3, x4] = lines[j];
      const max = Math.max(x1, x3);
      const min = Math.min(x2, x4);
      if (min > max) commonLines.push([max, min]);
    }
  }

  commonLines.sort((a, b) => a[0] - b[0]);

  let totalOverlapLength = 0;
  let currentStart = -100;
  let currentEnd = -100;

  for (let [start, end] of commonLines) {
    if (start > currentEnd) {
      totalOverlapLength += currentEnd - currentStart;
      currentStart = start;
      currentEnd = end;
    } else {
      currentEnd = Math.max(currentEnd, end);
    }
  }

  totalOverlapLength += currentEnd - currentStart;
  return totalOverlapLength;
}