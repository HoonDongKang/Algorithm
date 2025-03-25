package ch01

class P1 {
    fun isPalindrome(s: String): Boolean {
        var start = 0;
        var end = s.length - 1;
        while (start < end) {
            when {
                !Character.isLetterOrDigit(s[start]) -> start++
                !Character.isLetterOrDigit((s[end])) -> end--
                else -> {
                    if (Character.isLetterOrDigit(s[start]) != Character.isLetterOrDigit(s[end])) return false

                }
            }
            start++;
            end--;
        }
        return true
    }
}

fun main() {
    val p1 = P1()

    println(p1.isPalindrome("race a car"))
}