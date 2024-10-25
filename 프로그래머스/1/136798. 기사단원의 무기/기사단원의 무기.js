const getDivisorLength = (num) => {
  let arr = [];

  for (let i = 1; i <= Math.sqrt(num); i++) {
    if (num % i === 0) {
      arr.push(i);
      if (i !== num / i) {
        arr.push(num / i);
      }
    }
  }
  return arr.length;
};

function solution(number, limit, power) {
  let result = [];
  for (let i = 1; i < number + 1; i++) {
    result.push(getDivisorLength(i));
  }
  return result.reduce((acc, cur) => {
    return (acc += cur > limit ? power : cur);
  }, 0);
}