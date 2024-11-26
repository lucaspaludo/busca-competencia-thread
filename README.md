# 📁 **File Organizer & Converter** 🛠️

> Um sistema eficiente para conversão de arquivos PDF para TXT, extração de informações relevantes (CNPJ, meses, anos) e organização automatizada de pastas no computador com base nos dados encontrados.

---

## 🚀 **Funcionalidades**

- **📄 Conversão de PDF para TXT:** Transforma documentos PDF em arquivos TXT para facilitar a leitura e manipulação de dados.
- **🔍 Busca por Dados Específicos:** Localiza e extrai CNPJ, meses e anos nos arquivos TXT.
- **📂 Organização Automatizada:** Cria e organiza pastas no computador utilizando as informações extraídas.
  - Estrutura baseada em: `CNPJ > Ano > Mês`
- **⚡ Processamento Rápido e Confiável:** Ideal para lidar com grandes volumes de arquivos.

---

## 🛠️ **Tecnologias Utilizadas**

- **Linguagem:** Python 🐍
- **Bibliotecas:**
  - `PyPDF2`: Para extração de texto dos PDFs.
  - `re`: Para identificação de padrões de CNPJ, meses e anos.
  - `os` e `shutil`: Para manipulação e organização de arquivos/pastas.

---

## 📦 **Pré-requisitos**

Certifique-se de ter os seguintes itens instalados no seu ambiente:

- **Python 3.8+**
- **Bibliotecas Necessárias:** Instale as dependências com o comando:
  ```bash
  pip install -r requirements.txt
