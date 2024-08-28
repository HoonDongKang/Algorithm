const BABBLING_LIST = ['aya', 'ye', 'woo', 'ma'];

function solution(babbling) {
  let answer = 0;
  babbling = babbling.map((word) => {
    BABBLING_LIST.forEach((el) => {
      while (word.includes(el)) {
        word = word.replace(el, ' ');
      }
    });
    return word;
  });

  return babbling.map((word) => word.trim()).filter((word) => word === '')
    .length;
}