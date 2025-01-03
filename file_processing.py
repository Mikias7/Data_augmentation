import os
import cv2

def loop_images():
    # Path to the folder containing images
    folder_path = "image folder path"

    # Get all image file names from the folder
    image_files = [
        f for f in os.listdir(folder_path)
        if f.endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tif', '.tiff'))
    ]

    # Loop through each image file
    for image_file in image_files:
        image_path = os.path.join(folder_path, image_file)
        
        #print(image_path)

    sorted_image_file = sorted(image_files)
    return sorted_image_file


def loop_annotations():
    # Path to the folder containing annotations
    folder_path = "annotation folder path"

    # Get all txt file from the folder
    txt_files = [
        f for f in os.listdir(folder_path)
        if f.endswith(('.txt'))
    ]

    # Loop through each txt file
    for txt_file in txt_files:
        txt_path = os.path.join(folder_path, txt_file)
        
        #print(txt_path)
    sorted_txt_file = sorted(txt_files)
    return sorted_txt_file
    
def save_img(image, image_name):
    
    # Output folder to save the modified image
    output_folder = "left_down_brightness_image"
    os.makedirs(output_folder, exist_ok=True)  

    # Save the image in the new folder
    output_path = os.path.join(output_folder, f"left_down_brightness_{image_name}")
    cv2.imwrite(output_path, image)

    print(f"Saved: {output_path}")

import os

import os

def save_annotation(annotation, annotation_name):
    """
    Reads a text file and saves its content to a new file in the 'new_annotation' folder.

    Parameters:
        annotation (str): The path to the input text file.
        annotation_name (str): The name to use for the output file.
    """
    # Output folder to save the annotation
    output_folder = "left_down_brightness_annotation"
    os.makedirs(output_folder, exist_ok=True)  

    # Read the content of the input file
    with open(annotation, 'r') as file:
        content = file.read()

    # Define the output path and save the content
    output_path = os.path.join(output_folder, f"left_down_brightness_{annotation_name}")

    with open(output_path, 'w') as file:
        file.write(content)

    print(f"Saved: {output_path}")
