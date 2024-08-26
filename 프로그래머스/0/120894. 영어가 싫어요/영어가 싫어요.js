const ENG_TO_NUM = [
  { text: 'zero', value: 0 },
  { text: 'one', value: 1 },
  { text: 'two', value: 2 },
  { text: 'three', value: 3 },
  { text: 'four', value: 4 },
  { text: 'five', value: 5 },
  { text: 'six', value: 6 },
  { text: 'seven', value: 7 },
  { text: 'eight', value: 8 },
  { text: 'nine', value: 9 },
];

function solution(numbers) {
  ENG_TO_NUM.forEach((el) => {
    numbers = numbers.replaceAll(el.text, el.value);
  });

  return +numbers;
}