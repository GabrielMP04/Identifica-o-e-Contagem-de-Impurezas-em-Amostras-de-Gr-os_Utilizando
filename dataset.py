from torch.utils.data import Dataset
from PIL import Image
import os

class GraosDataset(Dataset):

    def __init__(self, imagens, mascaras):
        self.imagens = imagens
        self.mascaras = mascaras

    def __len__(self):
        return len(self.imagens)

    def __getitem__(self, idx):

        imagem = Image.open(self.imagens[idx]).convert("RGB")
        mascara = Image.open(self.mascaras[idx])

        return imagem, mascara