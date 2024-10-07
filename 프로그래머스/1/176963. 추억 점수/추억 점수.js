function solution(name, yearning, photos) {
  const yearningMap = name.reduce((map, v, i) => {
    map.set(v, yearning[i]);
    return map;
  }, new Map());

  return photos.map((photo) =>
    photo.reduce(
      (acc, cur) => (acc += yearningMap.get(cur) ? yearningMap.get(cur) : 0),
      0
    )
  );
}
