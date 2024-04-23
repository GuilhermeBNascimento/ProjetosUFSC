function obterRegiaoFiscalAtravesDoCPFInformado(cpfInformado) {
    let nonoDigito = parseInt(cpfInformado.charAt(8));
    let regioes = ["RS",
        "DF, GO, MT, MS e TO",
        "AC, AP, AM, PA, RO e RR",
        "CE, MA e PI",
        "AL, PB, PE e RN",
        "BA e SE",
        "MG",
        "ES e RJ",
        "SP",
        "PR e SC"
    ];

    let regiaoFiscal = regioes[nonoDigito]
    console.log(cpfInformado)
    
    //----------------------------
    return regiaoFiscal
}



function tratadorDeCliqueExercicio8() {
    let textCPF = document.getElementById("textCPF")
	let textRegiao = document.getElementById("regiaoFiscal")

    const regiaoFiscal = obterRegiaoFiscalAtravesDoCPFInformado(textCPF.value);
    textRegiao.textContent = "Região fiscal: "+regiaoFiscal
}
