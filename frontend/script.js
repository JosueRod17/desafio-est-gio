const URL_API = "http://127.0.0.1:8000";

async function carregarContas() {

    const resposta = await fetch(`${URL_API}/contas`);

    const contas = await resposta.json();

    const tabela = document.getElementById("lista-contas");

    tabela.innerHTML = "";

    contas.forEach(conta => {

        tabela.innerHTML += `
            <tr>
                <td>${conta.id}</td>
                <td><strong>${conta.titular}</strong></td>
                <td>${conta.tipo}</td>
                <td class="${conta.saldo < 0 ? 'negativo' : 'positivo'}"> ${conta.saldo.toLocaleString("pt-BR",{style:"currency",currency:"BRL"})}

                </td>
            </tr>
        `;

    });

}

async function realizarSaque() {

    const idConta = Number(document.getElementById("idConta").value);
    const valor = Number(document.getElementById("valorSaque").value);

    const resposta = await fetch(`${URL_API}/saque`, {

        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify({

            id_conta: idConta,
            valor: valor

        })

    });

    const dados = await resposta.json();

    if (resposta.ok) {

        mostrarMensagem("Saque realizado com sucesso!", false);

        carregarContas();
        document.getElementById("idConta").value = "";
        document.getElementById("valorSaque").value = "";

    } else {

        mostrarMensagem(dados.detail, true);

    }

}

async function realizarTransferencia() {

    const origem = Number(document.getElementById("origem").value);

    const destino = Number(document.getElementById("destino").value);

    const valor = Number(document.getElementById("valorTransferencia").value);

    const resposta = await fetch(`${URL_API}/transferencia`, {

        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify({

            id_conta_origem: origem,
            id_conta_destino: destino,
            valor: valor

        })

    });

    const dados = await resposta.json();

    if (resposta.ok) {

        mostrarMensagem("Transferência realizada com sucesso!", false);

        carregarContas();
        document.getElementById("origem").value = "";
        document.getElementById("destino").value = "";
        document.getElementById("valorTransferencia").value = "";

    } else {

        mostrarMensagem(dados.detail, true);

    }

}

function mostrarMensagem(texto, erro = false) {

    const mensagem = document.getElementById("mensagem");

    mensagem.textContent = texto;

    mensagem.style.color = erro ? "#dc2626" : "#15803d";

}

window.onload = carregarContas;