def contar_graos(resultado):

    labels = resultado["labels"]

    sadios = 0
    impurezas = 0

    for label in labels:

        if label == 1:
            sadios += 1

        elif label == 2:
            impurezas += 1

    return sadios, impurezas