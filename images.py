from PIL import Image
import sys
import os

#gets the arguments from your command prompt i.e python3 arg1 arg2 arg3
current_dir = sys.argv[1] #folder with images
new_dir = sys.argv[2] #folder to save manipulated images

#create the folder is no exists
if os.path.exists(new_dir):
    print("Already exists")
else:
    os.makedirs(new_dir)

#iterates over the files in the original folder and perfoms a specific action
for entry in os.scandir(current_dir):
  if entry.is_file():  # Check if it's a file
    print(entry.name)
    img = Image.open(f"{current_dir}/{entry.name}")
    grayscale_img = img.convert("L")
    grayscale_img.save(f"{new_dir}/{entry.name}")
    print(f"Converting {entry.name} Done")
