# target_img = '/home/pala-peshmarga/Downloads/Photos/todo_icon.webp'
# result_img = '/home/pala-peshmarga/Downloads/Photos/result.webp'

import sys
import os
from rembg import remove
from PIL import Image

def remove_background(input_image_path, output_image_path):
    try:
        input_image = Image.open(input_image_path)
        output_image = remove(input_image)
        output_image.save(output_image_path, format="PNG")
        print(f"[Success] Saved to: {output_image_path}")
    except Exception as e:
        print(f"[Error] processing image: {e}")

if __name__ == "__main__":
    target_img = None
    
    script_dir = os.path.dirname(os.path.abspath(__file__))
    result_img = os.path.join(script_dir, "result.png")

    for arg in sys.argv[1:]:
        if arg.startswith("target="):
            target_img = arg.split("target=", 1)[1]
        elif arg.startswith("saveto="):
            result_img = arg.split("saveto=", 1)[1]

    if not target_img:
        print("[Error]: You must provide a target image.")
        print("Usage: python bgRemover.py target=/path/to/img.jpg [saveto=/path/to/out.png]")
        sys.exit(1)

    if not os.path.exists(target_img):
        print(f"[Error]: Input file does not exist at '{target_img}'")
        sys.exit(1)

    remove_background(target_img, result_img)
