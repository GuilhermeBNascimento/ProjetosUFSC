function mostrarApenasHome(){
    document.getElementById("divHome").setAttribute("style", "display: block");
    document.getElementById("login-body").setAttribute("style", "display: none");
    document.getElementById("nova-conta").setAttribute("style", "display: none");
}

function mostrarApenasLogin(){
    document.getElementById("divHome").setAttribute("style", "display: none");
    document.getElementById("nova-conta").setAttribute("style", "display: none");
    document.getElementById("login-body").setAttribute("style", "display: block");
    document.getElementById("login-email").value = ""
    document.getElementById("login-password").value = ""
}

function mostrarApenasConta(){
    document.getElementById("divHome").setAttribute("style", "display: none");
    document.getElementById("login-body").setAttribute("style", "display: none");
    document.getElementById("nova-conta").setAttribute("style", "display: block");
}

document.getElementById("botaoLogin").disabled = true;
document.getElementById("login-email").addEventListener("keydown", stateHandle);
document.getElementById("login-password").addEventListener("keydown", stateHandle);

function stateHandle(){
    if (document.getElementById("login-email").value === "" || document.getElementById("login-password").value === ""){
        document.getElementById("botaoLogin").disabled = true;
    }else{
        document.getElementById("botaoLogin").disabled = false;
    }
}