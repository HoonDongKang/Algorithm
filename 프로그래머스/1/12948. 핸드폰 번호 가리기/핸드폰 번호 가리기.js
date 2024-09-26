function solution(phone_number) {
    const length = phone_number.length
    return Array(length-4).fill("*").join("").concat(phone_number.slice(-4))
}