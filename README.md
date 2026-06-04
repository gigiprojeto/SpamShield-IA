# 🛡️ SpamShield IA — Detector Inteligente de Spam com Machine Learning

<p align="center">
  <img src="https://img.shields.io/badge/Python-Backend-blue?style=for-the-badge&logo=python" />
  <img src="https://img.shields.io/badge/Flask-API-black?style=for-the-badge&logo=flask" />
  <img src="https://img.shields.io/badge/SQLite-Database-003B57?style=for-the-badge&logo=sqlite" />
  <img src="https://img.shields.io/badge/HTML5-Frontend-orange?style=for-the-badge&logo=html5" />
  <img src="https://img.shields.io/badge/CSS3-Design-blue?style=for-the-badge&logo=css3" />
  <img src="https://img.shields.io/badge/JavaScript-Interface-yellow?style=for-the-badge&logo=javascript" />
  <img src="https://img.shields.io/badge/Machine%20Learning-TF--IDF%20%2B%20Naive%20Bayes-green?style=for-the-badge" />
</p>

<p align="center">
  Sistema inteligente para detecção automática de mensagens de spam utilizando técnicas de Processamento de Linguagem Natural (NLP) e Machine Learning.
</p>

---

# 📌 Sobre o Projeto

O SpamShield IA é um projeto acadêmico desenvolvido para demonstrar a aplicação prática de Inteligência Artificial na classificação automática de mensagens de texto.

A aplicação permite que o usuário envie uma mensagem por meio de uma interface web moderna e receba uma classificação instantânea indicando se o conteúdo é considerado SPAM ou NÃO SPAM.

Diferente de uma simples simulação por palavras-chave, o sistema utiliza um modelo de Machine Learning treinado com dados reais, proporcionando uma classificação mais inteligente e próxima dos filtros utilizados em plataformas de email.

---

# 🎯 Objetivos

Este projeto foi desenvolvido com o objetivo de aplicar conceitos de:

* Inteligência Artificial;
* Machine Learning;
* Processamento de Linguagem Natural (NLP);
* Classificação de Texto;
* Desenvolvimento Web Full Stack;
* APIs REST;
* Banco de Dados Relacional.

---

# 🚀 Funcionalidades

✅ Interface moderna e responsiva

✅ Classificação automática de mensagens

✅ Integração Frontend e Backend

✅ API REST desenvolvida em Flask

✅ Modelo de Machine Learning treinado com TF-IDF e Naive Bayes

✅ Armazenamento de consultas em banco SQLite

✅ Registro do histórico de análises

✅ Estrutura organizada para estudos e portfólio

---

# 🛠️ Tecnologias Utilizadas

## Frontend

* HTML5
* CSS3
* JavaScript

## Backend

* Python
* Flask
* Flask-CORS

## Banco de Dados

* SQLite

## Ciência de Dados e Machine Learning

* Pandas
* Scikit-Learn
* TF-IDF Vectorizer
* Multinomial Naive Bayes

## Ferramentas

* Visual Studio Code
* Git
* GitHub

---

# 📂 Estrutura do Projeto

```bash
SpamShield-IA/
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── backend/
│   ├── app.py
│   ├── criar_banco.py
│   ├── train_model.py
│   │
│   ├── database/
│   │   └── spamshield.db
│
│
├── dataset/
│   └── spam.csv
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

# 🧠 Como o Sistema Funciona

O funcionamento do SpamShield IA ocorre em quatro etapas principais:

### 1. Coleta da Mensagem

O usuário digita uma mensagem na interface web.

### 2. Pré-processamento

O texto é convertido em um formato adequado para análise.

### 3. Vetorização TF-IDF

A mensagem é transformada em dados numéricos por meio da técnica TF-IDF (Term Frequency - Inverse Document Frequency).

### 4. Classificação

O modelo Multinomial Naive Bayes analisa os padrões aprendidos durante o treinamento e retorna:

```plaintext
🚨 SPAM
```

ou

```plaintext
✅ NÃO SPAM
```

---

# 💾 Banco de Dados

Todas as análises realizadas podem ser armazenadas no banco SQLite.

Tabela utilizada:

```sql
CREATE TABLE historico (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    mensagem TEXT,
    resultado TEXT
);
```

Isso permite registrar o histórico das classificações realizadas pelo sistema.

---

# ⚙️ Como Executar o Projeto

## 1️⃣ Clonar o Repositório

```bash
git clone https://github.com/seu-usuario/spamshield-ia.git
```

---

## 2️⃣ Acessar a Pasta

```bash
cd spamshield-ia
```

---

## 3️⃣ Instalar Dependências

```bash
pip install -r requirements.txt
```

---

## 4️⃣ Criar o Banco de Dados

```bash
python backend/criar_banco.py
```

---

## 5️⃣ Treinar o Modelo

```bash
python backend/train_model.py
```

---

## 6️⃣ Executar o Backend

```bash
python backend/app.py
```

Servidor iniciado em:

```plaintext
http://localhost:5000
```

---

## 7️⃣ Executar o Frontend

Abra o arquivo:

```plaintext
frontend/index.html
```

ou utilize a extensão Live Server do Visual Studio Code.

---

# 🧪 Exemplos de Teste

### Entrada

```plaintext
Parabéns! Você ganhou um prêmio exclusivo.
```

### Saída Esperada

```plaintext
🚨 SPAM
```

---

### Entrada

```plaintext
Oi, vamos estudar amanhã?
```

### Saída Esperada

```plaintext
✅ NÃO SPAM
```

---

# 📚 Conceitos Aplicados

Durante o desenvolvimento deste projeto foram utilizados conceitos fundamentais da área de Tecnologia da Informação:

* Inteligência Artificial;
* Machine Learning;
* Processamento de Linguagem Natural;
* Classificação de Texto;
* Vetorização de Dados;
* APIs REST;
* Banco de Dados SQLite;
* Desenvolvimento Web Full Stack.

---

# 📊 Status do Projeto

<p align="center">
  🚀 Projeto em evolução contínua 🚀
</p>

Versão atual:

* Frontend funcional;
* Backend em Flask;
* Banco de dados SQLite;
* Modelo de Machine Learning treinado;
* Integração completa entre interface e IA.

---

# 👩‍💻 Autora

**Giovanna Dias**

Estudante de Ciência da Computação | Desenvolvedora em formação

Projeto desenvolvido com fins acadêmicos e para composição de portfólio profissional.

---

# ⭐ Considerações Finais

O SpamShield IA demonstra como técnicas modernas de Machine Learning podem ser aplicadas para resolver problemas reais de segurança digital. O projeto combina desenvolvimento web, ciência de dados e inteligência artificial em uma solução prática para classificação automática de mensagens, servindo como uma importante experiência de aprendizado e portfólio na área de tecnologia.
