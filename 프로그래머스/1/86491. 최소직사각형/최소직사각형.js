function solution(sizes) {
    sizes = sizes.map(size => size.sort((a, b) => b - a));

    const maxWidth = Math.max(...sizes.map(size => size[0]));
    const maxHeight = Math.max(...sizes.map(size => size[1]));

    return maxWidth * maxHeight;
}