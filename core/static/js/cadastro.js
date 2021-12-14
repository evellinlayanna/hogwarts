var senha = document.getElementById('senha')
var senha2 = document.getElementById('senha2')
var erro = document.getElementById('erro')
var erro2 = document.getElementById('erro2')
var email = document.getElementById('email')
var erro3 = document.getElementById('erro3')


function validar() {
    if (email.value == '') {
        erro3.innerText = ('Campo obrigatório')
        return false
    }
    else if (email.value != '') {
        erro3.innerText = ('')
    }
    if (senha.value == '') {
        erro.innerText = ('Campo obrigatório')
        return false
    }
    else if (senha.value.length < 6) {
        erro.innerText = ('Senha muito curta (Min 6 caracteres')
        return false
    }
    if (senha2.value != senha.value) {
        erro2.innerText = ('Senhas não coincidem')
        return false
    }
}