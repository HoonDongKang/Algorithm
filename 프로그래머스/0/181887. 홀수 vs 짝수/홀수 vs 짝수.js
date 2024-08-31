function solution(num_list) {
  let odd = 0;
  let even = 0;
  num_list.forEach((num, i) => {
    if ((i + 1) % 2 === 0) {
      even += num;
    } else {
      odd += num;
    }
  });

  return even > odd ? even : odd;
}
