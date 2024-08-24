function solution(message) {
    return message.replaceAll('"').length * 2;
}