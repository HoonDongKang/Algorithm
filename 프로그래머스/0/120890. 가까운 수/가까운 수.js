function solution(array, n) {
    let closest = array[0];
    let minDifference = Math.abs(n - closest);

    for (let i = 1; i < array.length; i++) {
        const currentDifference = Math.abs(n - array[i]);

        if (currentDifference < minDifference || 
            (currentDifference === minDifference && array[i] < closest)) {
            closest = array[i];
            minDifference = currentDifference;
        }
    }

    return closest;
}
