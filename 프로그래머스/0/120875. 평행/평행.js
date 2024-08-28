const getSlope = ([x1, y1], [x2, y2]) => {
  return (y2 - y1) / (x2 - x1);
};
function solution(dots) {
  const [A, B, C, D] = dots;

  const slopes = [
    [getSlope(A, B), getSlope(C, D)],
    [getSlope(A, C), getSlope(B, D)],
    [getSlope(A, D), getSlope(B, C)],
  ];

  return slopes.some(([slope1, slope2]) => slope1 === slope2) ? 1 : 0;
}