from PIL import Image
import random
import glob

# DEFINITIONS
class Avatar:
    def __init__(self, directory):
        self.directory = directory
        self.images = self.load_images()
        self.resize_values = {}  # Dictionary to store unique resize values


    def load_images(self):
        image_files = glob.glob(self.directory + '/*.png')  # Change '*.png' to the file extension of your images
        return image_files

    def get_random_image(self):
        if self.images:
            return random.choice(self.images)
        else:
            return None

# assign directories
head_directory = "/Users/aaa/Projects/generative_nft_v1/generative_assets/head 2"
mouth_directory = "/Users/aaa/Projects/generative_nft_v1/generative_assets/mouth"
ally_directory = "/Users/aaa/Projects/generative_nft_v1/generative_assets/allies"
background_directory = "/Users/aaa/Projects/generative_nft_v1/generative_assets/background images"
hair_directory = "/Users/aaa/Projects/generative_nft_v1/generative_assets/resized_hair"
eyes_directory = "/Users/aaa/Projects/generative_nft_v1/generative_assets/resized_eyes"
eyebrows_directory = "/Users/aaa/Projects/generative_nft_v1/generative_assets/eyebrows 2"
outfits_directory = "/Users/aaa/Projects/generative_nft_v1/generative_assets/outfits 2"

## INIT
# create avatar obj
head = Avatar(head_directory)
mouth_directory = Avatar(mouth_directory)
ally = Avatar(ally_directory)
background = Avatar(background_directory)
hair = Avatar(hair_directory)
eyes = Avatar(eyes_directory)
eyebrows_directory = Avatar(eyebrows_directory)
outfits = Avatar(outfits_directory)

# Define a dictionary to store unique resize values for hair images
hair_resize_values = {
    "/Users/aaa/Projects/generative_nft_v1/generative_assets/resized_hair/black tuft test.png": (400, 400),  # Specify unique values for each image
    "hair_image2.png": (210, 260),
    "hair_image3.png": (215, 255),
    # Add more as needed
}

# create a reference to the randomly selected hair path
hair_random_image_path = hair.get_random_image()

# Open the background and ally images
background = Image.open(
    background.get_random_image()
)
ally = Image.open(
    ally.get_random_image()
)
body = Image.open(
    outfits.get_random_image()
)
head = Image.open(
    head.get_random_image()
)
eyes = Image.open(
    eyes.get_random_image()
)
menu = Image.open(
    "/Users/aaa/Projects/generative_nft_v1/generative_assets/attack menu done/spacing rpg attack.png"
)
hair = Image.open(
    hair_random_image_path
)
eyebrows = Image.open(
    eyebrows_directory.get_random_image()
)
mouth = Image.open(
    mouth_directory.get_random_image()
)


# Resize the background and ally images
background = background.resize((500, 500))
ally = ally.resize((150, 150))
head = head.resize((200, 200))
eyes = eyes.resize((100, 100))
body = body.resize((175, 175))
menu = menu.resize((475, 550))

## HAIR UPDATES
# create a default hair resize value to use if 
default_hair_resize_value = (100, 100)

# select the corresponding resize values based on the provided hair image, using default value if hair path not in hair_resize_values
hair_resize_value = hair_resize_values.get(hair_random_image_path) if hair_random_image_path in hair_resize_values else default_hair_resize_value

# resize hair
hair = hair.resize(hair_resize_value)

eyebrows = eyebrows.resize((120, 90))
mouth = mouth.resize((25,25))

# Calculate the position to paste the ally image in the bottom left corner
x_position = 0
ally_y_position = background.height - ally.height

head_x_position = ((background.width - head.width) // 2)
head_y_position = ((background.height - head.height) // 2) - 10

body_x_position = ((background.width - body.width) // 2) + 15
body_y_position = background.height - body.height

menu_x_position = (background.width - menu.width) // 2
menu_y_position = ((background.height - menu.height) // 2) - 50

hair_x_position = ((background.width - hair.width) // 2) + 5
hair_y_position = ((background.height - hair.height) // 2) - 35

eyebrows_x_position = ((background.width - eyebrows.width) // 2) + 35
eyebrows_y_position = ((background.height - eyebrows.height) // 2) - 60

eyes_x_position = (((background.width - head.width) // 2)) + 90
eyes_y_position = (((background.height - head.height) // 2)) + 30

mouth_x_position = ((background.width - mouth.width) // 2) + 45
mouth_y_position = ((background.height - mouth.height) // 2) + 50

# Paste the ally image onto the background while preserving the alpha layer
background.paste(ally, (x_position, ally_y_position), ally)
background.paste(head, (head_x_position, head_y_position), head)
background.paste(body, (body_x_position, body_y_position), body)
background.paste(eyebrows, (eyebrows_x_position, eyebrows_y_position), eyebrows)
background.paste(eyes, (eyes_x_position, eyes_y_position), eyes)
background.paste(hair, (hair_x_position, hair_y_position), hair)
background.paste(mouth, (mouth_x_position, mouth_y_position), mouth)
background.paste(menu, (menu_x_position, menu_y_position), menu)

# Save the result
background.save("test.png", quality=95)
