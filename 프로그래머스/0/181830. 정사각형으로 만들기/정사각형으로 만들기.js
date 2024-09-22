function solution(arr) {
  const row = arr.length;
  const column = arr[0].length;

  if (row < column) {
    const add = Array(column).fill(0);
    while (arr.length < column) {
      arr.push([...add]);
    }
    return arr;
  }

  if (row > column) {
    return arr.map((el) => {
      const missingColumns = row - column;
      return [...el, ...Array(missingColumns).fill(0)];
    });
  }

  return arr;
}