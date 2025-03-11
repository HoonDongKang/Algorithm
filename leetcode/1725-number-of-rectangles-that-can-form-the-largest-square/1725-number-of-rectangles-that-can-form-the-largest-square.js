/**
 * @param {number[][]} rectangles
 * @return {number}
 */
var countGoodRectangles = function(rectangles) {
    const largest = Math.max(...rectangles.map(rectangle => Math.min(...rectangle)));

    return rectangles.reduce((acc, rectangle) => {
        if (Math.min(...rectangle) === largest) {
            acc++;
        }
        return acc;
    }, 0);
};
