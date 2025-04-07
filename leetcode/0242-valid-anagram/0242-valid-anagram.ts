function isAnagram(s: string, t: string): boolean {
        if (s.length !== t.length) return false;

        let alphabetArr = new Array(26).fill(0);

        for (let i = 0; i < s.length; i++) {
            alphabetArr[s.charCodeAt(i) - 97]++;
            alphabetArr[t.charCodeAt(i) - 97]--;
        }

        return alphabetArr.every((char) => char === 0);
};