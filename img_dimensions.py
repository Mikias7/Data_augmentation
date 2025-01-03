from PIL import Image

def get_img_dimensions(image_path):
    # Open an image file
    with Image.open(image_path) as img:
        # Get the width and height of the image
        width, height = img.size

    print(f"Width: {width}, Height: {height}") # w = 541 H = 560    dx_noramlized = 100 / 541 = 0.185
    return width, height