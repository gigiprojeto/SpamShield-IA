function analisarSpam() {

    let msg = document.getElementById("mensagem").value.toLowerCase();
    let resultado = document.getElementById("resultado");

    if (msg.trim() === "") {
        resultado.innerHTML = "⚠️ Digite uma mensagem!";
        resultado.style.color = "yellow";
        return;
    }

    let palavrasSpam = [
        "free",
        "ganhe",
        "dinheiro",
        "prize",
        "click",
        "clique",
        "urgente",
        "promoção",
        "vencedor",
        "prêmio",
        "bônus"
    ];

    let spam = palavrasSpam.some(p => msg.includes(p));

    if (spam) {
        resultado.innerHTML = "🚨 Resultado: SPAM";
        resultado.style.color = "#ef4444";
    } else {
        resultado.innerHTML = "✅ Resultado: NÃO É SPAM";
        resultado.style.color = "#22c55e";
    }
}
