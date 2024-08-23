function solution(money) {
    const COFFEE_PRICE = 5_500;
    const cups = Math.floor(money/COFFEE_PRICE)
    
    return [cups, money - cups*COFFEE_PRICE]
}