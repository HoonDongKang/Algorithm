const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let input = [];

rl.on('line', function (line) {
    input = [line];
}).on('close',function(){
    str = input[0];
    str = [...str].map((char) => String.fromCharCode(char.charCodeAt() > 95 ?  char.charCodeAt()-32 : char.charCodeAt() + 32) ).join("");
    console.log(str)
});