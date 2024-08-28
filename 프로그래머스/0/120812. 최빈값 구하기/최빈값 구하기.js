function solution(array) {
    const frequencyMap = new Map();
    
    for (let num of array) {
        frequencyMap.set(num, (frequencyMap.get(num) || 0) + 1);
    }

    let maxFrequency = 0;
    let mode = -1;
    for (let [num, frequency] of frequencyMap.entries()){
        if(frequency > maxFrequency){
            maxFrequency = frequency
            mode = num;
        } else if (frequency === maxFrequency) {
            mode = -1;
        }
    } 
    return mode;
}