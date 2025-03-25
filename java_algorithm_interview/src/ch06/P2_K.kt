package ch06

class P2_K {
    fun reverseString(s: CharArray): Unit {
        var start = 0;
        var end = s.size - 1

        while (start < end) {
            s[start] = s[end].also { s[end] = s[start] };
            start++;
            end--;
        }
    }
}

fun main() {
    val p2 = P2_K();
    val arr = charArrayOf('h', 'e', 'l', 'l', 'o');
    var string = p2.reverseString(arr)
    println(string);
}