function solution(myString, pat) {
  const index = myString.lastIndexOf(pat);
  
  return myString.substring(0, index + pat.length);
}