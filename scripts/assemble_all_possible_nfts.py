from PIL import Image
import glob
import os

# Define the paths to the folders containing the images
background_folder = "/Users/jaylowe/Projects/generative_nft_v1/generative_assets/background images/"
allies_folder = "/Users/jaylowe/Projects/generative_nft_v1/generative_assets/allies/"
heads_folder = "/Users/jaylowe/Projects/generative_nft_v1/generative_assets/heads/"
menu_folder = "/Users/jaylowe/Projects/generative_nft_v1/generative_assets/attack menu done/"
hair_folder = "/Users/jaylowe/Projects/generative_nft_v1/generative_assets/hair/"
eyebrows_folder = "/Users/jaylowe/Projects/generative_nft_v1/generative_assets/eyebrows/"
mouth_folder = "/Users/jaylowe/Projects/generative_nft_v1/generative_assets/mouth/"

# Get a list of image files in each folder using glob
background_files = glob.glob(os.path.join(background_folder, "*.png"))
allies_files = glob.glob(os.path.join(allies_folder, "*.png"))
heads_files = glob.glob(os.path.join(heads_folder, "*.png"))
menu_files = glob.glob(os.path.join(menu_folder, "*.png"))
hair_files = glob.glob(os.path.join(hair_folder, "*.png"))
eyebrows_files = glob.glob(os.path.join(eyebrows_folder, "*.png"))
mouth_files = glob.glob(os.path.join(mouth_folder, "*.png"))

# Loop through all the images in the folders
for background_file in background_files:
    for ally_file in allies_files:
        for head_file in heads_files:
            for menu_file in menu_files:
                for hair_file in hair_files:
                    for eyebrows_file in eyebrows_files:
                        for mouth_file in mouth_files:
                            # Open the images
                            background = Image.open(background_file)
                            ally = Image.open(ally_file)
                            head = Image.open(head_file)
                            menu = Image.open(menu_file)
                            hair = Image.open(hair_file)
                            eyebrows = Image.open(eyebrows_file)
                            mouth = Image.open(mouth_file)

                            # Resize the images (insert your resizing logic here)
                            # Resize the background and ally images
                            background = background.resize((500, 500))
                            ally = ally.resize((150, 150))
                            head = head.resize((400, 400))
                            menu = menu.resize((500, 500))
                            hair = hair.resize((200, 200))
                            eyebrows = eyebrows.resize((100, 100))
                            mouth = mouth.resize((50, 50))

                            # Calculate the positions (insert your position calculation logic here)
                            x_position = 0
                            ally_y_position = background.height - ally.height

                            head_x_position = ((background.width - head.width) // 2)
                            head_y_position = ((background.height - head.height) // 2) + 49

                            menu_x_position = (background.width - menu.width) // 2
                            menu_y_position = (background.height - menu.height) // 2

                            hair_x_position = (background.width - hair.width) // 2
                            hair_y_position = (background.height - hair.height) // 2

                            eyebrows_x_position = ((background.width - eyebrows.width) // 2) + 25
                            eyebrows_y_position = ((background.height - eyebrows.height) // 2) + 10

                            mouth_x_position = ((background.width - mouth.width) // 2) + 50
                            mouth_y_position = ((background.height - mouth.height) // 2) + 75

                            # Paste the images onto the background (insert your paste logic here)
                            background.paste(ally, (x_position, ally_y_position), ally)
                            background.paste(head, (head_x_position, head_y_position), head)
                            background.paste(menu, (menu_x_position, menu_y_position), menu)
                            background.paste(hair, (hair_x_position, hair_y_position), hair)
                            background.paste(eyebrows, (eyebrows_x_position, eyebrows_y_position), eyebrows)
                            background.paste(mouth, (mouth_x_position, mouth_y_position), mouth)

                            # Save the result with a unique name based on the input image filenames
                            background_name = os.path.splitext(os.path.basename(background_file))[0]
                            ally_name = os.path.splitext(os.path.basename(ally_file))[0]
                            head_name = os.path.splitext(os.path.basename(head_file))[0]
                            menu_name = os.path.splitext(os.path.basename(menu_file))[0]
                            hair_name = os.path.splitext(os.path.basename(hair_file))[0]
                            eyebrows_name = os.path.splitext(os.path.basename(eyebrows_file))[0]
                            mouth_name = os.path.splitext(os.path.basename(mouth_file))[0]
                            output_filename = f"/Users/jaylowe/Projects/generative_nft_v1/generative_assets/generation_results/output_{background_name}_{ally_name}_{head_name}_{menu_name}_{hair_name}_{eyebrows_name}_{mouth_name}.png"
                            background.save(output_filename, quality=95)
