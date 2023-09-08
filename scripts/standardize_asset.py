from PIL import Image
import glob
import os

dir = "/Users/jaylowe/Projects/generative_nft_v1/generative_assets/eyes 2"

images = glob.glob(os.path.join(dir, "*.png"))

for image in images:
    opened_img = Image.open(image)
    resized_img = opened_img.resize((221,114))
    name = os.path.splitext(os.path.basename(image))[0]
    resized_img.save(f"/Users/jaylowe/Projects/generative_nft_v1/generative_assets/resized_eyes/{name}.png")