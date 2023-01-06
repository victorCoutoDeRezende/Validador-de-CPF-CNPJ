from CPF_CNPJ import Documento

def mensagem_abertura(msg):
    tamanho = len(msg)
    print("-=" * tamanho)
    print(msg.center(tamanho * 2))
    print("-=" * tamanho)
    print("\n")

def pergunta_doc():
    mensagem_abertura("Verifique um documento CPF ou CNPJ")

    doc = Documento.cria_documento(input("CPF/CNPJ -> "))

    print(doc)

pergunta_doc()