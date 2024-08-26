function solution(spell, dic) {
  for (let word of dic) {
    if (spell.every((char) => word.includes(char))) {
      return 1;
    }
  }
  return 2;
}
