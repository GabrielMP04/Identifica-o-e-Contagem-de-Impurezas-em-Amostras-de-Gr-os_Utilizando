import torch
import torchvision

from torch.utils.data import DataLoader

from src.graos_dataset import GraosDataset


def collate_fn(batch):
    return tuple(zip(*batch))


dataset = GraosDataset(
    "dataset/imagens",
    "annotations.json"
)

loader = DataLoader(
    dataset,
    batch_size=2,
    shuffle=True,
    collate_fn=collate_fn
)

model = torchvision.models.detection.maskrcnn_resnet50_fpn(
    weights="DEFAULT"
)

device = torch.device(
    "cuda"
    if torch.cuda.is_available()
    else "cpu"
)

model.to(device)

imagens, targets = next(iter(loader))

imagens = [
    img.to(device)
    for img in imagens
]

targets = [
    {
        k: v.to(device)
        for k, v in t.items()
    }
    for t in targets
]

model.train()

loss_dict = model(
    imagens,
    targets
)

print("\nLosses encontradas:\n")

for nome, valor in loss_dict.items():
    print(
        nome,
        "=",
        valor.item()
    )