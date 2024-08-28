function solution(score) {
  const average = score.map(([english, math], index) => ({
    index: index,
    average: (english + math) / 2,
  }));

  average.sort((a, b) => b.average - a.average);

  const ranks = new Array(average.length);

  let currentRank = 1;

  for (let i = 0; i < average.length; i++) {
    if (i > 0 && average[i].average < average[i - 1].average) {
      currentRank = i + 1;
    }
    ranks[average[i].index] = currentRank;
  }

  return ranks;
}