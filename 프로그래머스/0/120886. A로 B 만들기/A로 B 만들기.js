function solution(before, after) {
    const beforeArr = [...before];
    const afterArr = [...after];
    
    for (let char of afterArr) {
        if(beforeArr.indexOf(char) !== -1){
            beforeArr.splice(beforeArr.indexOf(char), 1)
        } else return 0;
    }
    
    return 1
}