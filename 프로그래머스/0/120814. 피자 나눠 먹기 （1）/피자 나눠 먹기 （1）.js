function solution(n) {
    const PIZZA_PIECES = 7;
    
    let pizzas = 1; 
    while(PIZZA_PIECES * pizzas < n) pizzas ++;
    
    return pizzas
}