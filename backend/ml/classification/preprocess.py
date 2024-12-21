import os
from PIL import Image

# Paths
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
RAW_DATA_PATH = os.path.join(BASE_DIR, "../../data/raw/")
PROCESSED_DATA_PATH = os.path.join(BASE_DIR, "../../data/processed/image/")

# Garment categories and subfolders (e.g., skirt types)
categories = {
    "skirt": ["2-panel", "4-panel", "8-panel"],
    "t-shirts": [],
    "dress": [],
    "jacket": [],
}

# Create processed directories
for category, subfolders in categories.items():
    if not subfolders:  # Categories without subfolders (e.g., t-shirts)
        os.makedirs(os.path.join(PROCESSED_DATA_PATH, "front", category), exist_ok=True)
        os.makedirs(os.path.join(PROCESSED_DATA_PATH, "back", category), exist_ok=True)
    else:  # Categories with subfolders (e.g., skirt types)
        for subfolder in subfolders:
            os.makedirs(os.path.join(PROCESSED_DATA_PATH, "front", category, subfolder), exist_ok=True)
            os.makedirs(os.path.join(PROCESSED_DATA_PATH, "back", category, subfolder), exist_ok=True)

# Function to resize and save images
def resize_and_save(input_path, output_path, size=(224, 224)):
    try:
        img = Image.open(input_path).convert("RGB")
        img = img.resize(size)
        img.save(output_path)
    except Exception as e:
        print(f"Error processing {input_path}: {e}")

# Preprocess images
for category, subfolders in categories.items():
    category_path = os.path.join(RAW_DATA_PATH, category)
    if not subfolders:  # No subfolders (e.g., t-shirts)
        for garment_folder in os.listdir(category_path):
            garment_path = os.path.join(category_path, garment_folder)
            if os.path.isdir(garment_path):
                # Front image
                front_img = os.path.join(garment_path, f"{garment_folder}_camera_front.png")
                if os.path.exists(front_img):
                    output_path = os.path.join(PROCESSED_DATA_PATH, "front", category, f"{garment_folder}_front.png")
                    resize_and_save(front_img, output_path)
                # Back image
                back_img = os.path.join(garment_path, f"{garment_folder}_camera_back.png")
                if os.path.exists(back_img):
                    output_path = os.path.join(PROCESSED_DATA_PATH, "back", category, f"{garment_folder}_back.png")
                    resize_and_save(back_img, output_path)
    else:  # Subfolders exist (e.g., skirt types)
        for subfolder in subfolders:
            subfolder_path = os.path.join(category_path, subfolder)
            for garment_folder in os.listdir(subfolder_path):
                garment_path = os.path.join(subfolder_path, garment_folder)
                if os.path.isdir(garment_path):
                    # Front image
                    front_img = os.path.join(garment_path, f"{garment_folder}_camera_front.png")
                    if os.path.exists(front_img):
                        output_path = os.path.join(PROCESSED_DATA_PATH, "front", category, subfolder, f"{garment_folder}_front.png")
                        resize_and_save(front_img, output_path)
                    # Back image
                    back_img = os.path.join(garment_path, f"{garment_folder}_camera_back.png")
                    if os.path.exists(back_img):
                        output_path = os.path.join(PROCESSED_DATA_PATH, "back", category, subfolder, f"{garment_folder}_back.png")
                        resize_and_save(back_img, output_path)
