import torch
import torchvision
from PIL import Image
from torchvision import transforms

device = torch.device(
    "cuda" if torch.cuda.is_available() else "cpu"
)

model = torchvision.models.detection.maskrcnn_resnet50_fpn()

model.load_state_dict(
    torch.load(
        "modelos/maskrcnn_graos.pth",
        map_location=device
    )
)

model.eval()

transform = transforms.ToTensor()

def analisar(caminho):

    imagem = Image.open(caminho).convert("RGB")

    tensor = transform(imagem)

    with torch.no_grad():
        resultado = model([tensor])[0]

    return resultado