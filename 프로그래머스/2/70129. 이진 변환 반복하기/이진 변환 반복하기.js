function solution(s) {
    let zeroCount = 0;
    let count = 0;
    while (s !== "1") {
        const currentLength = s.length;
        s = s.replace(/0/g, "");
        zeroCount += currentLength - s.length;
        
        s = s.length.toString(2);

        count++;
    }
    return [count, zeroCount]
}