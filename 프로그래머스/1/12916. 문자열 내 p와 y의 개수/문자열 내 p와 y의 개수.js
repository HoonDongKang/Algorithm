function solution(s){
    const chars = s.toUpperCase().split("");
    const pCounts = chars.filter((char) => char === "P").length;
    const yCounts = chars.filter((char) => char === "Y").length;
    
    if(!pCounts && !yCounts) return true
    return pCounts === yCounts ? true : false;
}