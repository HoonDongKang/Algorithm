function solution(chicken) {
  let totalServiceChicken = 0;
  let coupons = chicken;

  while (coupons >= 10) {
    let serviceChicken = Math.floor(coupons / 10);

    totalServiceChicken += serviceChicken;

    coupons = (coupons % 10) + serviceChicken;
  }

  return totalServiceChicken;
}