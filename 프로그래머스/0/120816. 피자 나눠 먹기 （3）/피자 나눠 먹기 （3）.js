function solution(slice, n) {
    let count = 0;
    while (slice * count < n) count ++;
    return count;
}