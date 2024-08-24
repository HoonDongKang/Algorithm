const winning = (number) => {
    switch (number) {
        case "2":
            return "0";
            break;
            
        case "0":
            return "5";
            break;
            
        case "5":
            return "2";
            break;
    }
}

function solution(rsp) {
    return [...rsp].reduce((acc, number) => acc + winning(number), "")
}