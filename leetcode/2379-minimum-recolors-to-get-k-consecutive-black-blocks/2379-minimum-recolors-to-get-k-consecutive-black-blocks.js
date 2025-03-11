/**
 * @param {string} blocks
 * @param {number} k
 * @return {number}
 */
var minimumRecolors = function (blocks, k) {
    const maximumIndex = blocks.length - k;
    let arr = [];
    for (let i = 0; i <= maximumIndex; i++) {
        const block = blocks.slice(i, i + k);
        const wInBlockCount = [...block].reduce((acc, cur) => {
            if (cur === 'W') acc++;
            return acc;
        }, 0);

        arr.push(wInBlockCount)
    }
    return Math.min(...arr)
};  