const SYMBOLTABLE: { [key: string]: number } = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,
};

function romanToInt(s: string): number {
    const reverseStr = [...s].reverse();
    let result = 0;
    let prevValue = 0;

    for (let i = 0; i < reverseStr.length; i++) {
        const curRoman = reverseStr[i];
        const curValue = SYMBOLTABLE[curRoman];

        if (curValue < prevValue) {
            result -= curValue;
        } else {
            result += curValue;
        }
        
        prevValue = curValue;
    }

    return result;
}