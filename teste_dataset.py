from src.graos_dataset import GraosDataset

dataset = GraosDataset(
    "dataset/imagens",
    "annotations.json"
)

print("Quantidade de imagens:")
print(len(dataset))

imagem, target = dataset[0]

print("Shape da imagem:")
print(imagem.shape)

print("Labels:")
print(target["labels"])