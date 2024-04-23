function inverter() {
    let string = window.prompt("Digite sua string");
    let novastring = "";

    for (let i = string.length-1; i>=0; i--) {
        novastring += string[i];
    }
    console.log(novastring);
}

