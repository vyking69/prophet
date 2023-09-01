from PIL import Image
import random
import glob

class Character:
    def __init__(self, directory):
        self.directory = directory
        self.images = self.load_images()

    def load_images(self):
        image_files = glob.glob(self.directory + '/*.png')  # Change '*.png' to the file extension of your images
        return image_files

    def get_random_image(self):
        if self.images:
            return random.choice(self.images)
        else:
            return None

head_directory = "/Users/jaylowe/Projects/generative_nft_v1/generative_assets/heads"
ally_directory = "/Users/jaylowe/Projects/generative_nft_v1/generative_assets/allies"
background_directory = "/Users/jaylowe/Projects/generative_nft_v1/generative_assets/background images"
hair_directory = "/Users/jaylowe/Projects/generative_nft_v1/generative_assets/hair"

head = Character(head_directory)
ally = Character(ally_directory)
background = Character(background_directory)
hair = Character(hair_directory)

random_head_image = head.get_random_image()
random_ally_image = ally.get_random_image()

# Open the background and ally images
background = Image.open(
    background.get_random_image()
)
ally = Image.open(
    ally.get_random_image()
)
body = Image.open(
    "/Users/jaylowe/Projects/generative_nft_v1/generative_assets/outfits/gold bomber.png"    
)
head = Image.open(
    head.get_random_image()
)
menu = Image.open(
    "/Users/jaylowe/Projects/generative_nft_v1/generative_assets/attack menu done/spacing rpg attack.png"
)
hair = Image.open(
    hair.get_random_image()
)
eyebrows = Image.open(
    "/Users/jaylowe/Projects/generative_nft_v1/generative_assets/eyebrows/thick.png"
)
mouth = Image.open(
    "/Users/jaylowe/Projects/generative_nft_v1/generative_assets/mouth/tongue.png"
)

# Resize the background and ally images
background = background.resize((500, 500))
ally = ally.resize((150, 150))
head = head.resize((200, 200))
body = body.resize((175, 175))
menu = menu.resize((500, 500))
hair = hair.resize((250, 350))
eyebrows = eyebrows.resize((100, 100))
mouth = mouth.resize((50,50))

# Calculate the position to paste the ally image in the bottom left corner
x_position = 0
ally_y_position = background.height - ally.height

head_x_position = ((background.width - head.width) // 2)
head_y_position = ((background.height - head.height) // 2)

body_x_position = ((background.width - body.width) // 2) + 25
body_y_position = background.height - body.height

menu_x_position = (background.width - menu.width) // 2
menu_y_position = (background.height - menu.height) // 2

hair_x_position = ((background.width - hair.width) // 2)
hair_y_position = ((background.height - hair.height) // 2)

eyebrows_x_position = ((background.width - eyebrows.width) // 2) + 35
eyebrows_y_position = ((background.height - eyebrows.height) // 2) - 20

mouth_x_position = ((background.width - mouth.width) // 2) + 45
mouth_y_position = ((background.height - mouth.height) // 2) + 70

# Paste the ally image onto the background while preserving the alpha layer
background.paste(ally, (x_position, ally_y_position), ally)
background.paste(head, (head_x_position, head_y_position), head)
background.paste(hair, (hair_x_position, hair_y_position), hair)
background.paste(body, (body_x_position, body_y_position), body)
background.paste(menu, (menu_x_position, menu_y_position), menu)
background.paste(eyebrows, (eyebrows_x_position, eyebrows_y_position), eyebrows)
background.paste(mouth, (mouth_x_position, mouth_y_position), mouth)

# Save the result
background.save("test.png", quality=95)
