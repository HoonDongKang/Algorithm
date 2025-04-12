function isPalindrome(s: string): boolean {
    let left = 0;
    let right = s.length - 1;

    while (left < right) {
        while (left < right && !isLetterOrDigit(s[left])) left++;
        while (left < right && !isLetterOrDigit(s[right])) right--;

        if (s[left].toLowerCase() !== s[right].toLowerCase()) return false;
        left++;
        right--;
    }

    return true;

    function isLetterOrDigit(c: string): boolean {
        return /[a-zA-Z0-9]/.test(c);
    }
}
