
import pandas as pd
import re
from pathlib import Path

# ==========================================
# CONFIGURAÇÕES
# ==========================================

ARQUIVO_ENTRADA = r"A.xlsx"
ARQUIVO_SAIDA = r"B.xlsx"

# ==========================================
# FUNÇÕES DE EXTRAÇÃO
# ==========================================

def limpar_texto(valor):
    if pd.isna(valor):
        return ""

    return re.sub(r"\s+", " ", str(valor)).strip()


def extrair_numero_sei(texto):
    resultado = re.search(
        r"OFÍCIO\s+SEI\s+N[º°.]?\s*(\d+)",
        texto,
        re.IGNORECASE
    )

    return resultado.group(1) if resultado else ""


def gerar_nome_arquivo(numero, texto):
    nome = f"OFICIO_SEI_N_{numero}_{texto}"

    nome = re.sub(r"[^a-zA-Z0-9_]", "_", nome)
    nome = re.sub(r"_+", "_", nome)

    return nome.strip("_")


def extrair_endereco(endereco):
    resultado = {
        "ENDERECO DO DESTINATARIO": "",
        "NUMERO DO DESTINATARIO": "",
        "COMPLEMENTO DO ENDERECO DO DESTINATARIO": "",
        "BAIRRO DESTINATARIO": ""
    }

    endereco = limpar_texto(endereco)

    if not endereco:
        return resultado

    # Exemplo: Rua Amador Bueno, 203, Centro
    partes = [p.strip() for p in endereco.split(",")]

    resultado["ENDERECO DO DESTINATARIO"] = partes[0]

    if len(partes) >= 2:
        numero = re.match(r"(\d+)", partes[1])

        if numero:
            resultado["NUMERO DO DESTINATARIO"] = numero.group(1)

            if len(partes) >= 3:
                resultado["BAIRRO DESTINATARIO"] = partes[2]

        else:
            resultado["COMPLEMENTO DO ENDERECO DO DESTINATARIO"] = partes[1]

            if len(partes) >= 3:
                resultado["BAIRRO DESTINATARIO"] = partes[2]

    return resultado


def extrair_cep_cidade_uf(texto):
    resultado = {
        "CEP DESTINATARIO": "",
        "CIDADE DESTINATARIO": "",
        "UF DO DSTINATARIO": ""
    }

    texto = limpar_texto(texto)

    # Exemplo: CEP: 11013-151 - Santos - SP
    padrao = re.search(
        r"(\d{5}-?\d{3})\s*[-,]\s*(.+?)\s*[-,]\s*([A-Z]{2})$",
        texto,
        re.IGNORECASE
    )

    if padrao:
        resultado["CEP DESTINATARIO"] = padrao.group(1)
        resultado["CIDADE DESTINATARIO"] = padrao.group(2).strip()
        resultado["UF DO DSTINATARIO"] = padrao.group(3).upper()

    return resultado


# ==========================================
# PROCESSAMENTO PRINCIPAL
# ==========================================

def processar_excel():

    entrada = Path(ARQUIVO_ENTRADA)

    if not entrada.exists():
        print("Arquivo de entrada não encontrado!")
        return

    df = pd.read_excel(entrada, header=None, dtype=str)

    resultados = []

    for _, linha in df.iterrows():

        # Mantém a posição original das colunas,
        # mesmo quando alguma célula está vazia.
        dados = [limpar_texto(v) for v in linha.tolist()]

        dados += [""] * (4 - len(dados))

        oficio = dados[0]
        destinatario = dados[1]
        endereco = dados[2]
        localidade = dados[3]

        # Ignora linhas completamente vazias.
        if not any(dados):
            continue

        numero = extrair_numero_sei(oficio)

        nome_arquivo = gerar_nome_arquivo(numero, oficio)

        endereco_extraido = extrair_endereco(endereco)
        localidade_extraida = extrair_cep_cidade_uf(localidade)

        resultado = {
            "NOTIFICACAO_SEI": numero,
            "NOME DO ARQUIVO COMPLEMENTAR": nome_arquivo,

            "NOME DO DESTINATARIO": (
                f"{oficio} {destinatario}".strip()
            ),

            **endereco_extraido,
            **localidade_extraida,

            "ETIQUETA DO OBJETO": ""
        }

        resultados.append(resultado)

    # Criação do Excel B
    df_saida = pd.DataFrame(resultados)

    df_saida.to_excel(
        ARQUIVO_SAIDA,
        index=False
    )

    print(f"Processamento concluído!")
    print(f"Registros processados: {len(resultados)}")
    print(f"Arquivo gerado: {ARQUIVO_SAIDA}")


if __name__ == "__main__":
    processar_excel()
