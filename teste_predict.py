from src.predict import (
    analisar_imagem,
    filtrar_resultados,
    contar_classes
)

resultado = analisar_imagem(
    "dataset/imagens/img001.jpeg"
)

resultado = filtrar_resultados(
    resultado,
    limiar=0.7
)

graos, impurezas = contar_classes(
    resultado
)

print()

print("================================")

print(
    "Quantidade de objetos:",
    len(resultado["labels"])
)

print(
    "Grãos Sadios:",
    graos
)

print(
    "Impurezas:",
    impurezas
)

print("================================")

print()

for i in range(
    len(resultado["labels"])
):

    label = resultado["labels"][i].item()

    score = (
        resultado["scores"][i]
        .item()
    )

    if label == 1:

        nome = "grao_sadio"

    elif label == 2:

        nome = "impureza"

    else:

        nome = "desconhecido"

    print(
        f"{i+1:02d} | "
        f"{nome} | "
        f"score={score:.3f}"
    )