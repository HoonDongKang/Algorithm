const list = {
  iceamericano: 4500,
  americanoice: 4500,
  hotamericano: 4500,
  americanohot: 4500,
  americano: 4500,
  anything: 4500,
};

function solution(order) {
    var answer = 0;
    order.forEach((el) => {
        answer += list[el] || 5000
    })
    return answer;
}