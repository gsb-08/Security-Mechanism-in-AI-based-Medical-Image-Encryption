import os
from PIL import Image
import matplotlib.pyplot as plt

# Point to your dataset
data_path = "data/raw/chest_xray/train/NORMAL/"

# Look at first image
image_files = os.listdir(data_path)[:5]
for img_file in image_files:
    img = Image.open(os.path.join(data_path, img_file))
    plt.imshow(img, cmap='gray')
    plt.title(img_file)
    plt.show()
    print(f"Image size: {img.size}")