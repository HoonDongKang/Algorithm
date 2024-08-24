function solution(box, n) {
    const [width, length, height] = box;
    
    return Math.floor(width/n) * Math.floor(length/n) * Math.floor(height/n)
}