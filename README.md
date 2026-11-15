# Extração e Estruturação de Dados de Ofícios SEI

Projeto desenvolvido em Python para automatizar a extração, transformação e organização de informações presentes em planilhas Excel relacionadas a ofícios do Sistema Eletrônico de Informações (SEI).

A aplicação realiza a leitura de uma planilha de entrada, identifica informações dos ofícios e destinatários, extrai dados de endereço e localidade e gera uma nova planilha Excel com os campos estruturados.

## 🚀 Funcionalidades

- Leitura automatizada de arquivos Excel.
- Extração de números de identificação de ofícios SEI por meio de expressões regulares (Regex).
- Geração automática de nomes padronizados para arquivos complementares.
- Identificação e separação de informações de endereços.
- Extração de números de endereço, complementos e bairros.
- Identificação de CEP, cidade e UF.
- Tratamento e normalização de textos.
- Identificação e desconsideração de linhas completamente vazias.
- Organização dos dados extraídos em colunas específicas.
- Exportação dos resultados para uma nova planilha Excel.

## 🛠️ Tecnologias utilizadas

- **Python 3.10+**
- **Pandas:** leitura, manipulação e estruturação de dados tabulares.
- **Regex (re):** identificação e extração de informações por padrões de texto.
- **Pathlib:** gerenciamento de caminhos e arquivos.
- **OpenPyXL:** suporte à leitura e escrita de arquivos Excel.

## 📁 Estrutura do projeto

```text
extracao-dados-oficios-sei/
│
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

## ⚙️ Instalação

1. Clone o repositório:

```bash
git clone https://github.com/Claudiohlm/extracao-dados-oficios-sei.git
```

2. Acesse a pasta:

```bash
cd extracao-dados-oficios-sei
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

## ▶️ Como utilizar

1. Coloque o arquivo Excel de entrada na pasta do projeto.
2. Configure os nomes dos arquivos nas variáveis:

```python
ARQUIVO_ENTRADA = "A.xlsx"
ARQUIVO_SAIDA = "B.xlsx"
```

3. Execute o programa:

```bash
python main.py
```

4. Após o processamento, o arquivo Excel de saída será gerado automaticamente.

## 📊 Organização dos dados

O programa utiliza quatro colunas de entrada:

| Coluna | Informação |
|---|---|
| 1 | Identificação do ofício |
| 2 | Destinatário |
| 3 | Endereço |
| 4 | Localidade (CEP, cidade e UF) |

Os dados são transformados e organizados em campos específicos, como:

- Número de identificação SEI.
- Nome do arquivo complementar.
- Nome do destinatário.
- Endereço do destinatário.
- Número do endereço.
- Complemento.
- Bairro.
- CEP.
- Cidade.
- UF.

## 🧠 Conceitos aplicados

Este projeto utiliza conceitos importantes de desenvolvimento e automação:

- **ETL:** extração, transformação e geração de dados estruturados.
- **Expressões regulares:** identificação de padrões em textos.
- **DataFrames:** manipulação e organização de dados tabulares.
- **Tratamento de exceções e validações:** verificação da existência do arquivo de entrada e tratamento de valores vazios.
- **Automação de processos:** redução de atividades manuais na organização de informações.

## ⚠️ Observações

- A planilha de entrada deve respeitar a estrutura de quatro colunas esperada pelo programa.
- Os padrões de extração de endereços e localidades dependem do formato dos dados de origem.
- O programa não altera a planilha original.
- Os arquivos Excel utilizados para testes não devem conter informações pessoais ou institucionais reais.



Estudante de Sistemas de Informação, com interesse em desenvolvimento Python, automação de processos, análise de dados e soluções para otimização de atividades administrativas.

- GitHub: [Claudiohlm](https://github.com/Claudiohlm)
