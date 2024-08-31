function solution(num_list) {
  const evenSum = num_list.filter((num) => num % 2 === 0).join('');

  const oddSum = num_list.filter((num) => num % 2 !== 0).join('');

  console.log(oddSum, evenSum);
  return +evenSum + +oddSum;
}