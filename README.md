# 📱 Gerador de QR Code em Python

Aplicação simples desenvolvida em Python para geração automática de imagens de QR Code a partir de links ou textos, exibida com contagem regressiva.

---

## 🛠️ Tecnologias Utilizadas

* **Python** (versão 3.10+)
* **[uv](https://astral.sh/uv)** - Gerenciador de projetos e ambientes virtuais
* **[qrcode](https://pypi.org/project/qrcode/)** - Biblioteca para geração de QR Codes
* **[Pillow](https://pypi.org/project/pillow/)** - Biblioteca de processamento de imagens

---

## 🌐 Arquitetura e Roadmap Web

Atualmente, o projeto executa via **Terminal**. O plano de evolução inclui a criação de uma interface gráfica web:

* **HTML5:** Estrutura e formulário para inserção do texto/URL.
* **CSS3:** Estilização moderna e responsiva da interface.
* **JavaScript:** Envio dos dados via requisição assíncrona (`fetch`) e atualização dinâmica do QR Code e do temporizador na tela.
* **Backend Python (FastAPI/Flask):** API que processará a requisição da web e retornará a imagem gerada.

---

## 🚀 Como Executar o Projeto

### Pré-requisitos
Certifique-se de ter o **Python** e o **[uv](https://astral.sh/uv)** instalados no seu sistema.

---

### Se preciso, garanta o pip na .venv

* python -m ensurepip --upgrade
* python -m pip install qrcode

---

### Passo a Passo

1. **Clone o repositório:**
   ```bash
   git clone [https://github.com/eamoriim/Gerador-de-QR-code.git](https://github.com/eamoriim/Gerador-de-QR-code.git)
   cd Gerador-de-QR-code