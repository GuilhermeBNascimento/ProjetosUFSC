function verificar() {
    let numero = parseInt(prompt("Informe o Número"));
    let intervalo = [30,50];
    let intervalo2 = [60,100];

    if ((numero>=intervalo[0]) && (numero<=intervalo[1])) {
       console.log(numero + "está no intervalo [30,50].");
    } else if((numero>=intervalo2[0]) && (numero<=intervalo2[1])) {
        console.log(numero + "está no intervalo [60,100].");
    }
    else {
        console.log("O número informado não está em nenhum dos dois intervalos.");
    }
    

}