"""
Fungsi-fungsi terkait model: membangun arsitektur, memuat checkpoint,
transformasi gambar, dan inferensi.
"""

import streamlit as st
import torch
import torch.nn as nn
import torchvision
from PIL import Image
from torchvision import transforms

from config import (
    CLASS_NAMES,
    IMAGENET_MEAN,
    IMAGENET_STD,
    IMG_SIZE,
    MODEL_NAME,
    MODEL_PATH,
)


def build_model(model_name: str, num_classes: int) -> nn.Module:
    """Membangun arsitektur model (bobot pretrained ImageNet tidak diunduh,
    karena akan langsung ditimpa oleh checkpoint hasil training)."""
    if model_name == "mobilenet_v2":
        model = torchvision.models.mobilenet_v2(weights=None)
        in_features = model.classifier[1].in_features
        model.classifier[1] = nn.Linear(in_features, num_classes)
    elif model_name == "efficientnet_b0":
        model = torchvision.models.efficientnet_b0(weights=None)
        in_features = model.classifier[1].in_features
        model.classifier[1] = nn.Linear(in_features, num_classes)
    else:
        raise ValueError(f"Model tidak dikenal: {model_name}")
    return model


@st.cache_resource(show_spinner=True)
def load_model():
    """Memuat model + checkpoint sekali saja (di-cache oleh Streamlit)."""
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model = build_model(MODEL_NAME, len(CLASS_NAMES))
    state_dict = torch.load(MODEL_PATH, map_location=device)
    model.load_state_dict(state_dict)
    model.to(device)
    model.eval()
    return model, device


eval_tfms = transforms.Compose(
    [
        transforms.Resize((IMG_SIZE, IMG_SIZE)),
        transforms.ToTensor(),
        transforms.Normalize(IMAGENET_MEAN, IMAGENET_STD),
    ]
)


@torch.no_grad()
def predict(image: Image.Image, model, device):
    """Menjalankan inferensi dan mengembalikan array probabilitas per kelas."""
    x = eval_tfms(image.convert("RGB")).unsqueeze(0).to(device)
    probs = model(x).softmax(1).cpu().numpy()[0]
    return probs