function solution(s, n) {
    let result = '';

    for (let i = 0; i < s.length; i++) {
        let char = s[i];

        if (char >= 'A' && char <= 'Z') {
            result += String.fromCharCode((char.charCodeAt(0) - 65 + n) % 26 + 65);
        }
        else if (char >= 'a' && char <= 'z') {
            result += String.fromCharCode((char.charCodeAt(0) - 97 + n) % 26 + 97);
        }
        else {
            result += char;
        }
    }

    return result;
}
