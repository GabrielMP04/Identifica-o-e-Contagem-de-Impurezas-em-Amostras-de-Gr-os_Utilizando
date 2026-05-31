from pycocotools.coco import COCO

coco = COCO("annotations.json")

print("Categorias:")
print(coco.loadCats(coco.getCatIds()))

print()

print("Quantidade de imagens:")
print(len(coco.getImgIds()))

print()

print("Quantidade de anotações:")
print(len(coco.getAnnIds()))