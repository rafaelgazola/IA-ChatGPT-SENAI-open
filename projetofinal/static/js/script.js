// URL base do backend Flask
const API = "/listar";

// Estado atual
let produtos = [];
let editandoId = null;

// ------------------------- NAVEGAÇÃO -------------------------
document.querySelectorAll(".topbar nav a").forEach(link => {
    link.addEventListener("click", e => {
        e.preventDefault();
        document.querySelectorAll(".topbar nav a").forEach(a => a.classList.remove("active"));
        link.classList.add("active");
        const view = link.dataset.view;
        document.querySelectorAll(".view").forEach(v => v.classList.remove("active"));
        document.getElementById("view-" + view).classList.add("active");
        if (view === "form") resetarForm();
    });
});

// ------------------------- FUNÇÕES GERAIS -------------------------
function mostrarToast(msg, tipo = "success") {
    const toast = document.getElementById("toast");
    toast.textContent = msg;
    toast.className = "toast " + tipo;
    toast.hidden = false;
    setTimeout(() => {
        toast.hidden = true;
    }, 2500);
}

function formatarMoeda(valor) {
    return Number(valor).toLocaleString("pt-BR", { style: "currency", currency: "BRL" });
}

// ------------------------- READ (GET) -------------------------
async function listarProdutos() {
    try {
        const res = await fetch(API);
        if (!res.ok) throw new Error("Falha ao buscar produtos");
        produtos = await res.json();
        renderProdutos();
    } catch (err) {
        mostrarToast(err.message, "error");
    }
}

function renderProdutos() {
    const busca = (document.getElementById("busca").value || "").toLowerCase();
    const container = document.getElementById("produtos-container");
    const vazio = document.getElementById("vazio");

    const filtrados = produtos.filter(p =>
        (p.nome || "").toLowerCase().includes(busca) ||
        (p.categoria || "").toLowerCase().includes(busca)
    );

    container.innerHTML = "";
    if (filtrados.length === 0) {
        vazio.hidden = false;
        return;
    }
    vazio.hidden = true;

    filtrados.forEach(p => {
        const card = document.createElement("div");
        card.className = "card";
        card.innerHTML = `
            <span class="nome">${escapeHtml(p.nome)}</span>
            <span class="categoria">${escapeHtml(p.categoria || "Sem categoria")}</span>
            <span class="valor">${formatarMoeda(p.valor)}</span>
            <span class="estoque">Estoque: ${p.estoque != null ? p.estoque : 0} un</span>
            <div class="acoes">
                <button class="btn-editar" onclick="iniciarEdicao(${p.id})">Editar</button>
                <button class="btn-deletar" onclick="deletarProduto(${p.id})">Excluir</button>
            </div>
        `;
        container.appendChild(card);
    });
}

function escapeHtml(texto) {
    const div = document.createElement("div");
    div.textContent = texto;
    return div.innerHTML;
}

// ------------------------- FORMULÁRIO -------------------------
document.getElementById("produto-form").addEventListener("submit", async e => {
    e.preventDefault();
    const nome = document.getElementById("nome").value.trim();
    const valor = parseFloat(document.getElementById("valor").value);

    if (!nome || isNaN(valor)) {
        mostrarToast("Preencha nome e valor corretamente.", "error");
        return;
    }

    const dados = {
        nome,
        valor,
        categoria: document.getElementById("categoria").value.trim() || "Sem categoria",
        estoque: parseInt(document.getElementById("estoque").value) || 0
    };

    try {
        let res;
        if (editandoId) {
            // UPDATE (PUT)
            res = await fetch(`/atualizar/${editandoId}`, {
                method: "PUT",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify(dados)
            });
        } else {
            // CREATE (POST)
            res = await fetch("/criar", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify(dados)
            });
        }

        if (!res.ok) throw new Error("Erro ao salvar produto");
        mostrarToast(editandoId ? "Produto atualizado!" : "Produto cadastrado!");
        resetarForm();
        irParaLista();
        listarProdutos();
    } catch (err) {
        mostrarToast(err.message, "error");
    }
});

// ------------------------- EDIÇÃO -------------------------
function iniciarEdicao(id) {
    const p = produtos.find(x => x.id === id);
    if (!p) return;

    editandoId = id;
    document.getElementById("produto-id").value = id;
    document.getElementById("nome").value = p.nome;
    document.getElementById("valor").value = p.valor;
    document.getElementById("categoria").value = p.categoria || "";
    document.getElementById("estoque").value = p.estoque != null ? p.estoque : 0;

    document.getElementById("form-titulo").textContent = "Editar Produto";
    document.getElementById("btn-salvar").textContent = "Salvar Alterações";

    document.querySelectorAll(".topbar nav a").forEach(a => a.classList.remove("active"));
    document.querySelector('.topbar nav a[data-view="form"]').classList.add("active");
    document.querySelectorAll(".view").forEach(v => v.classList.remove("active"));
    document.getElementById("view-form").classList.add("active");
}

function resetarForm() {
    editandoId = null;
    document.getElementById("produto-form").reset();
    document.getElementById("produto-id").value = "";
    document.getElementById("form-titulo").textContent = "Cadastrar Produto";
    document.getElementById("btn-salvar").textContent = "Salvar";
}

function irParaLista() {
    document.querySelectorAll(".topbar nav a").forEach(a => {
        a.classList.toggle("active", a.dataset.view === "list");
    });
    document.querySelectorAll(".view").forEach(v => {
        v.classList.toggle("active", v.id === "view-list");
    });
}

// ------------------------- DELETE -------------------------
async function deletarProduto(id) {
    if (!confirm("Tem certeza que deseja excluir este produto?")) return;
    try {
        const res = await fetch(`/apagar/${id}`, { method: "DELETE" });
        if (!res.ok) throw new Error("Erro ao excluir produto");
        mostrarToast("Produto removido com sucesso!");
        listarProdutos();
    } catch (err) {
        mostrarToast(err.message, "error");
    }
}

// ------------------------- INICIALIZAÇÃO -------------------------
listarProdutos();
