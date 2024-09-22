function solution(myStr) {
    let a = myStr.split(/[abc]/g).filter((char) => char)
  return a.length ? a : ['EMPTY'];
}