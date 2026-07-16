"""
Konfigurasi & konstanta aplikasi Tomato Leaf Doctor.
"""

MODEL_PATH = "checkpoints/mobilenet_v2_tomato_leaf_disease_final.pt"
MODEL_NAME = "mobilenet_v2"
IMG_SIZE = 224

IMAGENET_MEAN = [0.485, 0.456, 0.406]
IMAGENET_STD = [0.229, 0.224, 0.225]

# Urutan kelas HARUS sama persis dengan urutan class_names saat training
# (hasil ImageFolder, urut alfabetis)
CLASS_NAMES = [
    "Tomato___Bacterial_spot",
    "Tomato___Early_blight",
    "Tomato___Late_blight",
    "Tomato___Leaf_Mold",
    "Tomato___Septoria_leaf_spot",
    "Tomato___Spider_mites Two-spotted_spider_mite",
    "Tomato___Target_Spot",
    "Tomato___Tomato_Yellow_Leaf_Curl_Virus",
    "Tomato___Tomato_mosaic_virus",
    "Tomato___healthy",
]