function relativeSortArray(arr1: number[], arr2: number[]): number[] {
    const arr2Map = new Map();
    arr2.forEach((num, i) => arr2Map.set(num, i))

    arr1.sort((a, b) => {
        const aIdx = arr2Map.get(a)
        const bIdx = arr2Map.get(b)

        if (aIdx !== undefined && bIdx === undefined) {
            return -1
        }
        if (aIdx === undefined && bIdx !== undefined) {
            return 1
        }
        if (aIdx === undefined && bIdx === undefined) {
            return a - b;
        }

        return aIdx - bIdx
    })

    return arr1
};