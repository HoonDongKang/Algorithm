const generateMap = () => {
  let map = new Map();
  for (let i = 0; i < 10; i++) {
    map.set(i + '', String.fromCharCode(97 + i));
  }
  return map;
};

function solution(age) {
  let numbers = String(age);
  const map = generateMap();
  return [...numbers].map((number) => map.get(number)).join('');
}