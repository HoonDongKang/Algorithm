function solution(t, p) {
    const pl = p.length;
    let count = 0;

    for (let i = 0; i <= t.length - pl; i++) {
        const substr = t.slice(i, i + pl);
        
        if (substr <= p) {
            count++;
        }
    }

    return count;
}
