import json
import os
from PIL import Image

# Pasta onde estão as imagens e os JSONs
PASTA = "dataset/imagens"

coco = {
    "images": [],
    "annotations": [],
    "categories": [
        {
            "id": 1,
            "name": "grao_sadio"
        },
        {
            "id": 2,
            "name": "impureza"
        }
    ]
}

image_id = 1
annotation_id = 1

for arquivo in os.listdir(PASTA):

    if not arquivo.endswith(".json"):
        continue

    caminho_json = os.path.join(
        PASTA,
        arquivo
    )

    with open(
        caminho_json,
        "r",
        encoding="utf-8"
    ) as f:

        dados = json.load(f)

    # Nome base do arquivo
    base = os.path.splitext(arquivo)[0]

    caminho_img = None
    nome_imagem = None

    # Procura a imagem correspondente
    for ext in [
        ".jpg",
        ".jpeg",
        ".png",
        ".JPG",
        ".JPEG",
        ".PNG"
    ]:

        teste = os.path.join(
            PASTA,
            base + ext
        )

        if os.path.exists(teste):

            caminho_img = teste
            nome_imagem = base + ext

            break

    if caminho_img is None:

        print(
            f"[ERRO] Imagem não encontrada para: {arquivo}"
        )

        continue

    try:

        img = Image.open(caminho_img)

        largura, altura = img.size

    except Exception as erro:

        print(
            f"[ERRO] Não foi possível abrir {caminho_img}"
        )

        print(erro)

        continue

    coco["images"].append({
        "id": image_id,
        "file_name": nome_imagem,
        "width": largura,
        "height": altura
    })

    for shape in dados["shapes"]:

        label = shape["label"]

        if label == "grao_sadio":

            categoria = 1

        elif label == "impureza":

            categoria = 2

        else:

            print(
                f"[AVISO] Classe desconhecida: {label}"
            )

            continue

        pontos = shape["points"]

        segmentacao = []

        xs = []
        ys = []

        for x, y in pontos:

            segmentacao.extend([
                float(x),
                float(y)
            ])

            xs.append(x)
            ys.append(y)

        xmin = min(xs)
        xmax = max(xs)

        ymin = min(ys)
        ymax = max(ys)

        largura_bbox = xmax - xmin
        altura_bbox = ymax - ymin

        area = largura_bbox * altura_bbox

        bbox = [
            float(xmin),
            float(ymin),
            float(largura_bbox),
            float(altura_bbox)
        ]

        coco["annotations"].append({
            "id": annotation_id,
            "image_id": image_id,
            "category_id": categoria,
            "segmentation": [
                segmentacao
            ],
            "bbox": bbox,
            "area": float(area),
            "iscrowd": 0
        })

        annotation_id += 1

    print(
        f"[OK] Processado: {nome_imagem}"
    )

    image_id += 1

# Salva o COCO final
with open(
    "annotations.json",
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        coco,
        f,
        ensure_ascii=False,
        indent=4
    )

print("\n================================")
print("Conversão concluída com sucesso")
print(
    f"Imagens: {len(coco['images'])}"
)
print(
    f"Anotações: {len(coco['annotations'])}"
)
print("Arquivo: annotations.json")
print("================================")